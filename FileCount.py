import os
dir = "D:/Object Detection YOLO/Images"
count = 0
for file in os.listdir(dir):
    if os.path.exists(os.path.join(dir, file)):
        count = count + 1

print(count)