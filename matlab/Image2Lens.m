% pix dis
pix_right_dis = 0.13725;
pix_left_dis = 0.046;
% right image dis
right2image_dis = 14.5798;
right2left_lens_dis = 1200;
% left image dis
left2image_dis = 25.3451;
right_lens_pitch = 14.7;

imgSize_x = 3840;
imgSize_y = 2160;
right_len_x = 35;
right_len_y = 20;
left_len_x = 108;
left_len_y = 108;
real_pix_x = left_len_x * right_len_x;
real_pix_y = left_len_y * right_len_y;
read_pix_x_offset = (imgSize_x - real_pix_x) / 2+1;
read_pix_y_offset = (imgSize_y - real_pix_y) / 2;
angle = 72;

% pix_right_dis = 0.1;
% pix_left_dis = 0.2;
% % right image dis
% right2image_dis = 14.5798;
% right2left_lens_dis = 1000;
% % left image dis
% left2image_dis = 80;
% right_lens_pitch = 14.7;
% 
% imgSize_x = 20;
% imgSize_y = 20;
% right_len_x = 4;
% right_len_y = 4;
% left_len_x = 5;
% left_len_y = 5;
% real_pix_x = left_len_x * right_len_x;
% real_pix_y = left_len_y * right_len_y;
% read_pix_x_offset = (imgSize_x - real_pix_x) / 2+1;
% read_pix_y_offset = (imgSize_y - real_pix_y) / 2+1;
% angle = 72;

rsArr = zeros(imgSize_x,imgSize_y,3);

dict = mainDict( ...
    real_pix_x, real_pix_y, ...
    right_len_x, right_len_y,...
    angle,right_lens_pitch,pix_right_dis,...
    pix_left_dis,right2left_lens_dis, ...
    left2image_dis,right2image_dis ...
    );
% for pix_x=0:real_pix_x
%     for pix_y=0:real_pix_y
%         aa = str2num(dict(num2str([pix_x,pix_y])));
%         left_lens_x = aa(1);
%         left_lens_y= aa(2);
%         left_pix_x = aa(3);
%         left_pix_y= aa(4);
% %                left_pix_x = 50;
% %         left_pix_y= 50;
%         imgName = getImageName(left_lens_x, left_lens_y);
%         img = importdata(imgName);
%         rsArr(read_pix_x_offset + pix_x, read_pix_y_offset + pix_y,:) = img(left_pix_x+1,left_pix_y+1,:);
%         fprintf('x:%5d,y:%5d\n',pix_x,pix_y);
%     end
% end
for lens_x=0:left_lens_x
    for lens_y=0:left_lens_y
        imgName = getImageName(left_lens_x, left_lens_y);
        img = importdata(imgName);
        oneImageLoc = dict(left_lens_x, left_lens_y,:,:);
        for idx=1:length(oneImageLoc)
            pix_x_y = oneImageLoc(idx);
            aa = str2num(pix_x_y);
            origin_pix_x = aa(1);
            origin_pix_y= aa(2);
            pix_x = idx/800;
            pix_y = mod(idx,800);
            rsArr(read_pix_x_offset + origin_pix_x, read_pix_y_offset + origin_pix_y,:) = img(pix_x+1,pix_y+1,:);
            fprintf('x:%5d,y:%5d\n',origin_pix_x,origin_pix_y);
        end
            
            
    end
end
 

image(rsArr);
rsFilePath = strcat('image2Lens_',datestr(now),'.jpg');
fprintf(rsFilePath);
imwrite(rsArr,rsFilePath);

    
    
    
    