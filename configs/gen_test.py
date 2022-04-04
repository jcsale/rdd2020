# Generate Path for Test Images

import os

image_files = []
for filename in os.listdir("Data_India/val"):
    if filename.endswith(".jpg"):
        image_files.append("./Data_India/val" + filename)
        
with open("configs/test.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
