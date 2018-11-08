function [globalLeftId,localLeftId] = getLeftLensLocalId(globalPix, pixNum, lensNum)
    groupPixNum = pixNum / lensNum;
    globalLeftId = groupPixNum - mod(globalPix , groupPixNum) - 1;
    localLeftId = parseGlobal2Local(globalLeftId, groupPixNum);
end