%%return local lens id
function [globalId,mapping] = getPix2RightLensMapping(globalPix, pixNum, lensNum)
    groupPixNum = pixNum / lensNum;
    globalLensId = globalPix / groupPixNum;
    globalId = globalLensId;
    mapping = parseGlobal2Local(globalLensId, lensNum);
end