%% lens dis == y2
function dis =getLocalDis(localIdx, lens_num, pitch)
    odd = getOddTag(lens_num);
    if localIdx < 0
        dis =  (localIdx + 0.5 * odd) * pitch;
    else
        dis =  (localIdx - 0.5 * odd) * pitch;
    end
end