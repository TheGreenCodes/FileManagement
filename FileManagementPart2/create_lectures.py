import os
from pathlib import Path

sessions = [str(x) for x in range(1,21)]  # create 20sessions 
sessions = [str(0)+item if int(item) < 10 else item for item in sessions]

# Datastructuressession1Slide1.ppt

# get into the DataStructures directory
os.chdir('./DataStructures')


for item in sessions:
    # create 20 slides for each session
    for num in range(21):
        file_to_create = f"Datastructuressession{item}Slide{num}.ppt"
        Path(file_to_create).touch()
        # print(file_to_create)
