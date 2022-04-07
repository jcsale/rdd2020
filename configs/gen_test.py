# Generate Path for Test Images

import os

import os

image_files = []
for filename in os.listdir("./data/train/India/val"):
    if filename.endswith(".jpg"):
        image_files.append("data/train/India/val/" + filename)
        
with open("configs/test.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
