function dict = mainDict(imgSize_x, imgSize_y, right_len_x, right_len_y, angle,right_lens_pitch,pix_right_dis,pix_left_dis,right2left_lens_dis,left2image_dis,right2image_dis)
    dict = containers.Map();
    for pix_x = 0:imgSize_x
        for pix_y = 0:imgSize_y
            [left_lens_x, left_pix_x] = getOffsetPos(pix_x, imgSize_x, right_len_x, angle,right_lens_pitch,pix_right_dis,pix_left_dis,right2left_lens_dis,left2image_dis,right2image_dis);
            [left_lens_y, left_pix_y] = getOffsetPos(pix_y, imgSize_y, right_len_y, angle,right_lens_pitch,pix_right_dis,pix_left_dis,right2left_lens_dis,left2image_dis,right2image_dis);
            dict(num2str([pix_x, pix_y])) = num2str([left_lens_x, left_lens_y,left_pix_x,left_pix_y]);
        end
    end
end