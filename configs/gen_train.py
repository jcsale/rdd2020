# Generate Path for Train Images

import os

image_files = []
for filename in os.listdir("./data/RDD2020-2/train"):
    if filename.endswith(".jpg"):
        image_files.append("data/RDD2020-2/train/" + filename)
        
with open("configs/train.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
