import math
import numpy as np

from matplotlib import pyplot as plt
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import misc
import imageio
import time

## default size
## mm
pix_right_dis = 0.13725
pix_left_dis = 0.046
## left->right dis mm g1
right2image_dis = 14.5798
## mm
right2left_lens_dis = 1200
## mm g2
left2image_dis = 25.3451

## mm
right_lens_pitch = 14.7
# right_lens_pitch = 0.492 * 108

isDebug = False


def getLeftLensPitch(pixNum, lensNum):
    leftLensNum = pixNum / lensNum
    return (((leftLensNum - 1) * pix_right_dis * right2left_lens_dis) / right2image_dis) / (leftLensNum - 1)


def getOddTag(num):
    if num % 2 == 0:
        return 1
    else:
        return 0


###global 2 local
def parseGlobal2Local(global_loc, num):
    odd = getOddTag(num)
    mid = math.ceil(num / 2)
    diff = global_loc - mid
    if diff >= 0:
        return diff + 1 * odd
    else:
        return diff


##lens dis == y2
def getLocalDis(localIdx, lens_num, pitch):
    odd = getOddTag(lens_num)
    if localIdx < 0:
        return (localIdx + 0.5 * odd) * pitch
    else:
        return (localIdx - 0.5 * odd) * pitch


## y1 pix dis
def getPixDis(globalPix, pixNum, pix_dis):
    local = parseGlobal2Local(globalPix, pixNum)
    if isDebug:
        print("right pix local id:" + str(local))
    rightPixDis = getLocalDis(local, pixNum, pix_dis)
    if isDebug:
        print("rightPixDis:" + str(rightPixDis))
    return rightPixDis


##return local lens id

def getPix2RightLensMapping(globalPix, pixNum, lensNum):
    groupPixNum = pixNum / lensNum
    globalLensId = globalPix / groupPixNum
    return globalLensId, parseGlobal2Local(globalLensId, lensNum)


def getLeftLensLocalId(globalPix, pixNum, lensNum):
    groupPixNum = pixNum / lensNum
    groupId = groupPixNum - globalPix % groupPixNum - 1
    return groupId, parseGlobal2Local(groupId, groupPixNum)


def getY1(globalIdx, pixNum, pix_dis):
    return getPixDis(globalIdx, pixNum, pix_dis)


def getY2(localIdx, lens_num):
    return getLocalDis(localIdx, lens_num, right_lens_pitch)


def getY3(globalPix, pixNum, lensNum):
    leftLensNum = pixNum / lensNum
    (globalId, leftLensLocalId) = getLeftLensLocalId(globalPix, pixNum, lensNum)
    y3 = getLocalDis(leftLensLocalId, leftLensNum, getLeftLensPitch(pixNum, lensNum))
    if isDebug:
        print("y3 is:" + str(y3))
    return globalId, y3


### y4-y3=(y2-y1)*g2/g1
### g1=right2image_dis
### g2=left2image_dis
def getY4(globalPix, pixNum, lensNum):
    y1 = getY1(globalPix, pixNum, pix_right_dis)
    if isDebug:
        print("y1 is:" + str(y1))
    (rightLensGlobalId, localId) = getPix2RightLensMapping(globalPix, pixNum, lensNum)
    (leftLensGlobalId, y3) = getY3(globalPix, pixNum, lensNum)
    y2 = getY2(localId, lensNum)
    if isDebug:
        print("y2 is:" + str(y2))
    y4 = (y2 - y1) * left2image_dis / right2image_dis + y3
    if isDebug:
        print("y4 is:" + str(y4))
    return leftLensGlobalId, y3, y4


### g2=left2image_dis
def getImageSize(a):
    return 2 * left2image_dis * math.tan(a / 2.0 * math.pi / 180.0)


def getOffsetPos(globalPix, pixNum, lensNum, a):
    (leftLensGlobalId, y3, y4) = getY4(globalPix, pixNum, lensNum)
    return leftLensGlobalId, round((y4 - y3 + 0.5 * getImageSize(a)) / pix_left_dis)


def getImageName(x, y):
    realNum = str(x * 108 + y + 1).zfill(5)
    return "/Users/tang/export/Learn4xy/ParaImages/Para" + str(realNum) + ".jpg"


def main(imgSize_x, imgSize_y, right_len_x, right_len_y, angle):
    dict = {}
    for pix_x in range(0, imgSize_x):
        for pix_y in range(0, imgSize_y):
            if isDebug:
                print("pix id: x:" + str(pix_x) + " y:" + str(pix_y))
            (left_lens_x, left_pix_x) = getOffsetPos(pix_x, imgSize_x, right_len_x, angle)
            (left_lens_y, left_pix_y) = getOffsetPos(pix_y, imgSize_y, right_len_y, angle)
            dict[(pix_x, pix_y)] = ((int(left_lens_x), int(left_lens_y)), (int(left_pix_x), int(left_pix_y)))

    if isDebug:
        print("\n" + str(dict) + "\n")
    return dict


def createParamList(imgSize_x, imgSize_y, right_len_x, right_len_y, angle):
    list = []
    for pix_x in range(0, imgSize_x):
        for pix_y in range(0, imgSize_y):
            list.append((pix_x, pix_y, imgSize_x, imgSize_y, right_len_x, right_len_y, angle))
    return list


if __name__ == "__main__":
    # left_len_x = 108
    # left_len_y = 108
    # for len_x in range(0, left_len_x):
    #     for len_y in range(0, left_len_y):
    #         print(getImageName(len_x, len_y))
    start = time.localtime()
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
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
    #
    # imgSize_x = 20
    # imgSize_y = 20
    # right_len_x = 4
    # right_len_y = 4
    # real_pix_x = 20
    # real_pix_y = 20
    # read_pix_x_offset = (imgSize_x - real_pix_x) / 2
    # read_pix_y_offset = (imgSize_y - real_pix_y) / 2
    # left_len_x = 5
    # left_len_y = 5
    # angle = 72

    dict = main(real_pix_x, real_pix_y, right_len_x, right_len_y, angle)

    rsArr = np.zeros((imgSize_x, imgSize_y, 3), dtype=int)
    cnt = 0
    for pix_x in range(0, real_pix_x):
        for pix_y in range(0, real_pix_y):
            ((left_lens_x, left_lens_y), (left_pix_x, left_pix_y)) = dict[(pix_x, pix_y)]
            imgName = getImageName(left_lens_x, left_lens_y)
            # if cnt == 0:
            #     img = Image.fromarray(np.ones((1300, 1300, 3)), mode='RGB')
            # else:
            #     img = Image.fromarray(np.zeros((1300, 1300, 3)), mode='RGB')
            # cnt += 1
            #
            # rsArr[read_pix_x_offset + pix_x, read_pix_y_offset + pix_y] = img.getpixel((0,0))
            img = mpimg.imread(imgName)
            rsArr[read_pix_x_offset + pix_x, read_pix_y_offset + pix_y] = img[(int(left_pix_x), int(left_pix_y))]
            print("x_3:" + str(pix_x) + "\n y_3:" + str(pix_y))
            # mpimg.imread(imgName)
            # imFp = open(imgName, "rb")
            # img = Image.open(imFp)
            # rsArr[read_pix_x_offset + pix_x, read_pix_y_offset + pix_y] = img[(int(left_pix_x), int(left_pix_y))]
            # imFp.close()
    rs = Image.fromarray(rsArr,mode='RGB')
    rs.show()
    rs.save("image2lens_last.png")
    # imageio.imsave('image2lens_4.png', rsArr)
    print("cost time is:" + time.localtime() - start)
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # rsImg = Image.fromarray(rsArr)
    # rsImg.show()
    # rsImg.save('rs.tiff')
