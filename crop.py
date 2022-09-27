#!/usr/bin/python

import os
import sys, getopt

import yaml
from PIL import Image, ImageOps

with open('config.yaml') as file:
    try:
        config = yaml.safe_load(file)
    except yaml.YAMLError as exc:
        print(exc)

OUTPUT_FOLDER = config['OUTPUT_FOLDER']
QUALITY = config['QUALITY']


# Crop excess width or height
def crop(image, new_width, new_height):
    width, height = image.size
    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2

    # Crop the center of the image
    cropped_image = image.crop((left, top, right, bottom))
    return cropped_image

# Save to new file
def save(image, file_name):
    # extract the file name and extension
    split_tup = os.path.splitext(file_name)
    file_name = split_tup[0]
    file_extension = split_tup[1]
    final_name = file_name + '_thumbnail' + file_extension
    destination = OUTPUT_FOLDER + final_name
    image.save(destination, quality=QUALITY)

# Resize and crop image. Only process if mode of args given and exisiting image is same. I.e if args is potrait, only process potrait image
def process(img, new_width, new_height):
    image = Image.open(img)
    image = ImageOps.exif_transpose(image)
    horizontal=image.size[0] > image.size[1] and new_width > new_height
    vertical=image.size[0] < image.size[1] and new_width < new_height

    if horizontal:
        image.thumbnail(size=(image.size[0], new_height), resample=Image.ANTIALIAS)
        image = crop(image, new_width, new_height)
        save(image, img)
    elif vertical:
        image.thumbnail(size=(new_width, image.size[1]), resample=Image.ANTIALIAS)
        image = crop(image, new_width, new_height)
        save(image, img)
    else:
        msg = "Info: skip {file_name} because different mode"
        print(msg.format(file_name=img))

def main():
    new_height = ''
    new_width = ''
    file_name = ''
    path = ''

    ###############################
    # o == option
    # a == argument passed to the o
    ###############################
    # Cache an error with try..except
    # Note: options is the string of option letters that the script wants to recognize, with
    # options that require an argument followed by a colon (':') i.e. -h new_height
    try:
        myopts, args = getopt.getopt(sys.argv[1:],"h:w:i:p:")
    except getopt.GetoptError as e:
        print (str(e))
        print("Usage: %s -w new_width -h new_height -i input_file -p path_folder" % sys.argv[0])
        sys.exit(2)

    for o, a in myopts:
        if o == '-h':
            new_height=int(a)
        elif o == '-w':
            new_width=int(a)
        elif o == '-i':
            file_name=a
        elif o == '-p':
            path=a

    if len(path) > 0:
        # bulk
        images = [file for file in os.listdir(path) if file.endswith(('jpeg', 'png', 'jpg', 'JPEG', 'PNG', 'JPG'))]
        for img in images:
            process(img, new_width, new_height)
    elif len(file_name) > 0:
        # one file
        process(file_name, new_width, new_height)
    else:
        print("Pass")

if __name__=="__main__":
    main()
