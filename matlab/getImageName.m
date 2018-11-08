function path = getImageName(x,y)
    realNum = num2str(x * 108 + y + 1,'%05d');
    path =  "/Users/tang/export/Learn4xy/ParaImages/Para" + realNum + ".jpg";
end