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

## mm
# right_lens_pitch = 14.7
right_lens_pitch = 0.492
##
p_size_x = 3840
p_size_y = 2160

isDebug = False


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
    if isDebug:
        print("right pix local id:" + str(local))
    rightPixDis = getLocalDis(local, pixNum, p_right_dis)
    if isDebug:
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
    if isDebug:
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
    if isDebug:
        print("y1 is:" + str(y1))
    (rightLensGlobalId, localId) = getPix2LensMappingV2(globalPix, pixNum, lensNum)
    (leftLensGlobalId, y3) = getY3(globalPix, pixNum, lensNum)
    y2 = getY2(localId, lensNum)
    if isDebug:
        print("y2 is:" + str(y2))
    y4 = (y2 - y1) * left2image_dis / right2image_dis + y3
    if isDebug:
        print("y4 is:" + str(y4))
    return leftLensGlobalId, y4


### g2=left2image_dis
def getImageSize(a):
    return 2 * left2image_dis * math.tan(a / 2.0 * math.pi / 180.0)


def getOffsetPos(globalPix, pixNum, lensNum, a):
    (leftLensGlobalId, y4) = getY4(globalPix, pixNum, lensNum)
    (globalId, y3) = getY3(globalPix, pixNum, lensNum)
    return (leftLensGlobalId, round((y4 - y3 + 0.5 * getImageSize(a)) / p_left_dis))


def getImageName(x, y):
    realNum = str(x * 108 + y).zfill(5)
    return "G:\TwoPickupII\ParaImages\Para" + str(realNum) + ".jpg"


def main(imgSize_x, imgSize_y, right_len_x, right_len_y, angle):
    dict = {}
    for pix_x in range(0, imgSize_x):
        for pix_y in range(0, imgSize_y):
            if isDebug:
                print("pix id: x:" + str(pix_x) + " y:" + str(pix_y))
            (left_lens_x, left_pix_x) = getOffsetPos(pix_x, imgSize_x, right_len_x, angle)
            (left_lens_y, left_pix_y) = getOffsetPos(pix_y, imgSize_y, right_len_y, angle)
            dict[(pix_x, pix_y)] = ((left_lens_x, left_lens_y), (left_pix_x, left_pix_y))

    if isDebug:
        print("\n" + str(dict) + "\n")
    return dict


def createParamList(imgSize_x, imgSize_y, right_len_x, right_len_y, angle):
    list = []
    for pix_x in range(0, imgSize_x):
        for pix_y in range(0, imgSize_y):
            list.append((pix_x, pix_y, imgSize_x, imgSize_y, right_len_x, right_len_y, angle))
    return list


def threadPoolHandle((pix_x, pix_y, imgSize_x, imgSize_y, right_len_x, right_len_y, angle)):
    (left_lens_x, left_pix_x) = getOffsetPos(pix_x, imgSize_x, right_len_x, angle)
    (left_lens_y, left_pix_y) = getOffsetPos(pix_y, imgSize_y, right_len_y, angle)
    return ((left_lens_x, left_lens_y), (left_pix_x, left_pix_y))


from multiprocessing.dummy import Pool as ThreadPool

if __name__ == "__main__":
    # print(getImageName(107, 107))
    imgSize_x = 3840
    imgSize_y = 2160
    right_len_x = 35
    right_len_y = 20
    real_pix_x = 3780
    real_pix_y = 2160
    read_pix_x_offset = (imgSize_x - real_pix_x) / 2
    read_pix_y_offset = (imgSize_y - real_pix_y) / 2
    left_len_x = 108
    left_len_y = 108
    angle = 72

    params = createParamList(real_pix_x, real_pix_y, right_len_x, right_len_y, angle)
    pool = ThreadPool(4)
    dict = pool.map(threadPoolHandle, params)
    pool.close()
    pool.join()
    # dict = main(real_pix_x, real_pix_y, right_len_x, right_len_y, angle)
    # lensImg = {}
    # for len_x in range(0, left_len_x):
    #     for len_y in range(0, left_len_y):
    #         imgName = getImageName(left_len_x,left_len_y)
    #         lensImg[(len_x, len_y)] = Image.open(imgName)
    # rsArr = np.zeros((imgSize_x, imgSize_y))
    # for pix_x in range(0, real_pix_x):
    #     for pix_y in range(0, real_pix_y):
    #         ((left_lens_x, left_lens_y), (left_pix_x, left_pix_y)) = dict[(pix_x, pix_y)]
    #         imgName = getImageName(left_lens_x, left_lens_y)
    #         img = Image.open(imgName)
    #         rsArr[read_pix_x_offset + pix_x, read_pix_y_offset + pix_y] = img[(int(left_pix_x), int(left_pix_y))]
    # rsImg = Image.fromarray(rsArr)
    # rsImg.show()
    # rsImg.save('rs.tiff')
