#!/bin/python3
# move files to directories according to file name pattern

import os
import shutil
import glob


# get into the Datastructures directory
os.chdir('./DataStructures')

#take every file from the directory and add to a list for all files
all_files = [x for x in os.listdir('.')]

# make a set for the sessions present in the directory
# sessions = set((os.path.splitext(f)[0] for f in all_files))

# for session in sessions:
#     session_directory = session
#     os.mkdir(session)

#     for fname in glob.glob(f'*.{session[1:]}'):
#         shutil.move(fname, session_directory)


# Datastructuressession01Slide1.ppt
