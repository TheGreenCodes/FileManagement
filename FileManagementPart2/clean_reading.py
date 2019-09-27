#!/bin/python3
# move files to directories according to file name pattern

import os
import shutil


# get into the Datastructures directory
os.chdir('./DataStructures')

# Datastructuressession01Slide1.ppt
for f in os.listdir("."):
    folder_name = f[14:23]
    # print(folder_name)

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        shutil.move(f, folder_name)
    else:
        shutil.move(f, folder_name)
