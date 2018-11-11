import math
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time
import cv2
from PIL import ImageEnhance

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
        return int(diff + 1 * odd)
    else:
        return int(diff)


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
    # groupId = globalPix % groupPixNum
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
    return 2 * left2image_dis * math.tan(a / 2.0 * 3.14 / 180.0)


def getOffsetPos(globalPix, pixNum, lensNum, a):
    (leftLensGlobalId, y3, y4) = getY4(globalPix, pixNum, lensNum)
    return leftLensGlobalId, int((y4 - y3 + 0.5 * getImageSize(a)) / pix_left_dis)


def getImageName(x, y):
    realNum = str(x * 108 + y + 1).zfill(5)
    return "/Users/tang/export/Learn4xy/ParaImages/Para" + str(realNum) + ".jpg"


def main(imgSize_x, imgSize_y, right_len_x, right_len_y, angle):
    dict_lens_arr = []

    for x in range(0, imgSize_x):
        for y in range(0, imgSize_y):
            if isDebug:
                print("pix id: x:" + str(x) + " y:" + str(y))
            (left_lens_x, left_pix_x) = getOffsetPos(x, imgSize_x, right_len_x, angle)
            (left_lens_y, left_pix_y) = getOffsetPos(y, imgSize_y, right_len_y, angle)

            dict_lens_arr.append(((int(left_lens_x), int(left_lens_y)), (int(left_pix_x), int(left_pix_y), x, y)))
    dict_lens_arr.sort(key=lambda x: x[0])
    return dict_lens_arr


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
    left_len_x = 108
    left_len_y = 108
    real_pix_x = right_len_x * left_len_x
    real_pix_y = right_len_y * left_len_y
    read_pix_x_offset = (imgSize_x - real_pix_x) / 2
    read_pix_y_offset = (imgSize_y - real_pix_y) / 2

    angle = 72

    # imgSize_x = 20
    # imgSize_y = 20
    # right_len_x = 4
    # right_len_y = 4
    # left_len_x = 5
    # left_len_y = 5
    # real_pix_x = left_len_x * right_len_x
    # real_pix_y = left_len_y * right_len_y
    # read_pix_x_offset = (imgSize_x - real_pix_x) / 2
    # read_pix_y_offset = (imgSize_y - real_pix_y) / 2
    # angle = 72

    dict = main(real_pix_x, real_pix_y, right_len_x, right_len_y, angle)

    dictTime = time.localtime()
    print("cost generate dict time is:" + str(time.mktime(dictTime) - time.mktime(start)) + "s !!!")
    rsArr = np.zeros((imgSize_y, imgSize_x, 3), dtype=int)
    cnt = 0
    # for pix_x in range(0, real_pix_x):
    #     for pix_y in range(0, real_pix_y):
    #         ((left_lens_x, left_lens_y), (left_pix_x, left_pix_y)) = dict[(pix_x, pix_y)]
    #         imgName = getImageName(left_lens_x, left_lens_y)
    #         img = mpimg.imread(imgName)
    #         rsArr[read_pix_x_offset + pix_x, read_pix_y_offset + pix_y, :] = img[(int(left_pix_x), int(left_pix_y)), :]
    #         print("x_3:" + str(pix_x) + "\n y_3:" + str(pix_y))
    # for right2image_step in range(-10, 10):
    #     for left2image_step in range(-10, 10):
    #         for pix_right_step in range(-10, 10):
    #             for pix_left_step in range(-10, 10):
    #                 right2image_dis += right2image_step * 0.01
    #                 left2image_dis += left2image_step * 0.1
    #                 pix_right_dis += pix_right_step * 0.01
    #                 pix_left_dis += pix_left_step * 0.01
    (curImg_x, curImg_y) = -1, -1
    curLogTag = -1
    img = None
    for ((left_lens_x, left_lens_y), (left_pix_x, left_pix_y, x, y)) in dict:
        ## when lens switch then switch the image
        if (left_lens_x, left_lens_y) != (curImg_x, curImg_y):
            (curImg_x, curImg_y) = (left_lens_x, left_lens_y)
            print("yx_yx||x_:" + str(curImg_x) + " y_:" + str(curImg_y))
            imgName = getImageName(left_lens_y, left_lens_x)
            img = mpimg.imread(imgName)
        rsArr[read_pix_y_offset + y, read_pix_x_offset + x, :] = img[left_pix_y + 1, left_pix_x + 1, :]

    plt.imshow(rsArr)
    # cv2.equalizeHist(tmp)
    # ImageEnhance.Sharpness(rsArr)
    plt.imsave(
        "image2lens_" + right2image_dis + "_" + left2image_dis + "_" + pix_right_dis + "_" + pix_left_dis + "_" + str(
            time.mktime(time.localtime())) + ".png", rsArr)
    print("")
    print("cost image parse time is:" + str(
        time.mktime(time.localtime()) - time.mktime(dictTime)) + "s !!!")
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
