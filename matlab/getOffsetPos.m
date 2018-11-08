function [leftLensGlobalId,pos] = getOffsetPos(globalPix, pixNum, lensNum, a,right_lens_pitch,pix_right_dis,pix_left_dis,right2left_lens_dis,left2image_dis,right2image_dis)
    [leftLensGlobalId, y3, y4] = getY4(globalPix, pixNum, lensNum,right_lens_pitch,pix_right_dis,right2left_lens_dis,left2image_dis,right2image_dis);
    pos=round((y4 - y3 + 0.5 * getImageSize(a,left2image_dis)) / pix_left_dis);
end