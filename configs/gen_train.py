# Generate Path for Train Images

import os

image_files = []
for filename in os.listdir("Data_India/train/class1"):
    if filename.endswith(".jpg"):
        image_files.append("./Data_India/train/class1" + filename)
        
with open("configs/train.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
