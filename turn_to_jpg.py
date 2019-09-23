from os import listdir
import os
path = 'C:\\Users\\Olive\\Desktop\\spotlight_images\\'
onlyfiles = [f for f in listdir(path)]


for i in onlyfiles:
    old = path + i
    print(old)
    new = path + i + '.jpg'
    print(new)
    os.rename(old, new)