import os
from desaturate import process

img_dir = 'images/'
for img in os.listdir(img_dir):
    process(img_dir + img)
