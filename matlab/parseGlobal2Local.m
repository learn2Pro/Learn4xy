function localId = parseGlobal2Local(global_loc, num)
    odd = getOddTag(num);
    mid = ceil(num / 2);
    diff = global_loc - mid;
    if diff >= 0
        localId =  diff + 1 * odd;
    else
        localId =  diff;
    end
end
