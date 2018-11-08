function [globalId,y3] = getY3(globalPix, pixNum, lensNum,pix_right_dis,right2left_lens_dis,right2image_dis)
    leftLensNum = pixNum / lensNum;
    [globalId, leftLensLocalId] = getLeftLensLocalId(globalPix, pixNum, lensNum);
    y3 = getLocalDis(leftLensLocalId, leftLensNum, getLeftLensPitch(pixNum, lensNum,pix_right_dis,right2left_lens_dis,right2image_dis));
end