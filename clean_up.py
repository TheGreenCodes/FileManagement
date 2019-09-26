import os
import shutil
import glob


# get into the RandomFiles directory
os.chdir('./RandomFiles')

all_files = [x for x in os.listdir('.') ]

file_types = set((os.path.splitext(f)[1] for f in all_files))


for ftype in file_types:
    new_directory = ftype.replace(".", '')
    os.mkdir(new_directory)

    for fname in glob.glob(f'*.{ftype[1:]}'):
        shutil.move(fname, new_directory)
