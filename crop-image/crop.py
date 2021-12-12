#!/usr/bin/python

import os
import sys, getopt
from PIL import Image

new_height = ''
new_width = ''
file_name = ''

###############################
# o == option
# a == argument passed to the o
###############################
# Cache an error with try..except
# Note: options is the string of option letters that the script wants to recognize, with
# options that require an argument followed by a colon (':') i.e. -h new_height
try:
    myopts, args = getopt.getopt(sys.argv[1:],"h:w:i:")
except getopt.GetoptError as e:
    print (str(e))
    print("Usage: %s -w new_width -h new_height -i input_file " % sys.argv[0])
    sys.exit(2)

for o, a in myopts:
    if o == '-h':
        new_height=int(a)
    elif o == '-w':
        new_width=int(a)
    elif o == '-i':
        file_name=a

# PIL
im = Image.open(file_name)
width, height = im.size

left = (width - new_width)/2
top = (height - new_height)/2
right = (width + new_width)/2
bottom = (height + new_height)/2

# Crop the center of the image
im = im.crop((left, top, right, bottom))

# save file
split_tup = os.path.splitext(file_name)

# extract the file name and extension
file_name = split_tup[0]
file_extension = split_tup[1]
final_name = file_name + '-cropped' + file_extension
im.save(final_name)
