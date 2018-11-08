%% y1 pix dis
function pix_dis = getPixDis(globalPix, pixNum, pix_dis)
    local = parseGlobal2Local(globalPix, pixNum);
    rightPixDis = getLocalDis(local, pixNum, pix_dis);
    pix_dis =  rightPixDis;
end