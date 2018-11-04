import math
import numpy as np

from matplotlib import pyplot as plt
from PIL import Image

## default size
## mm
p_right_dis = 0.13725
p_left_dis = 0.046
## left->right dis mm g1
right2image_dis = 14.5798
## mm
right2left_lens_dis = 1200
## mm g2
left2image_dis = 25.3451


###input param
## right lens
right_lens_num_x = 35
right_lens_num_y = 19
## mm
# right_lens_pitch = 14.7
right_lens_pitch = 0.492
##
p_size_x = 3840
p_size_y = 2160


def getLeftLensNum():
    return p_size / right_lens_num


def getLeftLensPitch(pixNum, lensNum):
    leftLensNum = pixNum / lensNum
    return (((leftLensNum - 1) * p_right_dis * right2left_lens_dis) / right2image_dis) / (leftLensNum - 1)


def getOdd(num):
    if num % 2 == 0:
        return 1
    else:
        return 0


###global 2 local
def getLensLocal(lens_global_loc, lens_num):
    odd = getOdd(lens_num)
    mid = math.ceil(lens_num / 2)
    diff = lens_global_loc - mid
    if diff >= 0:
        return diff + 1 * odd
    else:
        return diff


##lens dis == y2
def getLocalDis(localIdx, lens_num, pitch):
    odd = getOdd(lens_num)
    if localIdx < 0:
        return -1.0 * ((-localIdx - 1.0 * odd) * pitch + 0.5 * pitch * odd)
    else:
        return (localIdx - 1.0 * odd) * pitch + 0.5 * pitch * odd


## y1 pix dis
def getPixDis(globalPix, pixNum):
    local = getLensLocal(globalPix, pixNum)
    print("right pix local id:" + str(local))
    rightPixDis = getLocalDis(local, pixNum, p_right_dis)
    print("rightPixDis:" + str(rightPixDis))
    return rightPixDis


##return local lens id

def getPix2LensMappingV2(globalPix, pixNum, lensNum):
    groupPixNum = pixNum / lensNum
    globalLensId = globalPix / groupPixNum
    return globalLensId, getLensLocal(globalLensId, lensNum)


def getY1(globalIdx, pixNum):
    return getPixDis(globalIdx, pixNum)


def getY2(localIdx, lens_num):
    return getLocalDis(localIdx, lens_num, right_lens_pitch)


def getY3(globalPix, pixNum, lensNum):
    leftLensNum = pixNum / lensNum
    (globalId, leftLensLocalId) = getLeftLensLocalId(globalPix, pixNum, lensNum)
    y3 = getLocalDis(leftLensLocalId, leftLensNum, getLeftLensPitch(pixNum, lensNum))
    print("y3 is:" + str(y3))
    return (globalId, y3)


def getLeftLensLocalId(globalPix, pixNum, lensNum):
    groupPixNum = pixNum / lensNum
    groupId = groupPixNum - globalPix % groupPixNum - 1
    return groupId, getLensLocal(groupId, groupPixNum)


### y4-y3=(y2-y1)*g2/g1
### g1=right2image_dis
### g2=left2image_dis
def getY4(globalPix, pixNum, lensNum):
    y1 = getY1(globalPix, pixNum)
    print("y1 is:" + str(y1))
    (rightLensGlobalId, localId) = getPix2LensMappingV2(globalPix, pixNum, lensNum)
    (leftLensGlobalId, y3) = getY3(globalPix, pixNum, lensNum)
    y2 = getY2(localId, lensNum)
    print("y2 is:" + str(y2))
    y4 = (y2 - y1) * left2image_dis / right2image_dis + y3
    print("y4 is:" + str(y4))
    return leftLensGlobalId, y4


### g2=left2image_dis
def getImageSize(a):
    return 2 * left2image_dis * math.tan(a / 2.0 * math.pi / 180.0)


def getOffsetPos(globalPix, pixNum, lensNum, a):
    (leftLensGlobalId, y4) = getY4(globalPix, pixNum, lensNum)
    (globalId, y3) = getY3(globalPix, pixNum, lensNum)
    return (leftLensGlobalId, round((y4 - y3 + 0.5 * getImageSize(a)) / p_left_dis))

def getImageName(x,y):
    realNum = (x*107+y).zfill(5)
    return "G:\TwoPickupII\ParaImages\Para"+str(realNum)+".jpg"

def main(imgSize, len, angle):
    dict = {}
    for pix_x in range(0, imgSize):
        for pix_y in range(0, imgSize):
            print("pix id: x:" + str(pix_x) + " y:" + str(pix_y))
            (left_lens_x, left_pix_x) = getOffsetPos(pix_x, imgSize, len, angle)
            (left_lens_y, left_pix_y) = getOffsetPos(pix_y, imgSize, len, angle)
            dict[(pix_x, pix_y)] = ((left_lens_x, left_lens_y), (left_pix_x, left_pix_y))

    print("\n" + str(dict) + "\n")
    return dict


if __name__ == "__main__":
    imgSize = 20
    right_len = 4
    left_len = imgSize / right_len
    angle = 72
    dict = main(imgSize, right_len, angle)
    lensImg = {}
    for len_x in range(0, left_len):
        for len_y in range(0, left_len):
            if len_y == 0 and len_x == 0:
                lensImg[(len_x, len_y)] = np.ones((800, 800)) * 256
            else:
                lensImg[(len_x, len_y)] = np.zeros((800, 800))
    rsArr = np.zeros((imgSize,imgSize))
    for pix_x in range(0, imgSize):
        for pix_y in range(0, imgSize):
            ((left_lens_x, left_lens_y), (left_pix_x, left_pix_y)) = dict[(pix_x, pix_y)]
            img = lensImg[(left_lens_x, left_lens_y)]
            rsArr[pix_x,pix_y] = img[(int(left_pix_x), int(left_pix_y))]
    rsImg = Image.fromarray(rsArr)
    rsImg.show()
    rsImg.thumbnail((imgSize,imgSize))
    rsImg.save('rs.tiff')
    # rsImg.save("rs.tiff")
