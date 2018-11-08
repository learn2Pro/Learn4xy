%%% y4-y3=(y2-y1)*g2/g1
%%% g1=right2image_dis
%%% g2=left2image_dis
function [leftGlobalId,y3,y4] = getY4(globalPix, pixNum, lensNum,right_lens_pitch,pix_right_dis,right2left_lens_dis,left2image_dis,right2image_dis)
    y1 = getY1(globalPix, pixNum, pix_right_dis);

    [~, localId] = getPix2RightLensMapping(globalPix, pixNum, lensNum);
    [leftGlobalId, y3] = getY3(globalPix, pixNum, lensNum,pix_right_dis,right2left_lens_dis,right2image_dis);
    y2 = getY2(localId, lensNum,right_lens_pitch);
    y4 = (y2 - y1) * left2image_dis / right2image_dis + y3;
end