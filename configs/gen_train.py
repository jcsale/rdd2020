# Generate Path for Train Images

import os

image_files = []
for filename in os.listdir("./data/train/India/train"):
    if filename.endswith(".jpg"):
        image_files.append("data/train/India/train/" + filename)
        
with open("configs/train.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
