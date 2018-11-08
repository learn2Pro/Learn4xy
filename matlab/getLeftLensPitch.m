function rs = getLeftLensPitch(pixNum, lensNum,pix_right_dis,right2left_lens_dis,right2image_dis)
    leftLensNum = pixNum / lensNum;
    rs = (((leftLensNum - 1) * pix_right_dis * right2left_lens_dis) / right2image_dis) / (leftLensNum - 1);
end