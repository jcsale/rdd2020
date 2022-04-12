# Generate Path for Test Images

import os

import os

image_files = []
for filename in os.listdir("./data/India+Czech-2/valid"):
    if filename.endswith(".jpg"):
        image_files.append("data/India+Czech-2/valid/" + filename)
        
with open("configs/test.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
