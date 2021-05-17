#!/usr/bin/python3
#  -*- coding: utf-8 -*-

# Date: Mon 17 May 2021 17:54:20 CEST
# Author: Nicolas Flandrois
# Last updated by: Nicolas Flandrois
# Last updated date: Mon 17 May 2021 17:54:20 CEST
# Description: How to convert back and forth base64 to/from image
import base64


# Convert an image file into a base64 text file

def get_base64_encoded_image(image_path):
    """Cette fonction va retourner l'encodage d'un fichier image,
    sous forme Base64."""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')


img_file = 'my_image.png'
with open("myimage_img.txt", 'w') as f:
    f.write(get_base64_encoded_image(img_file))


# Convert base64 text into image file
with open("myimage_img.txt", 'r') as f:
    imgstring = f.read()

imgdata = base64.b64decode(imgstring)
filename = 'my_new_image.png'  # Works also with jpg, change .png into .jpg
with open(filename, 'wb') as f:
    f.write(imgdata)
# f gets closed when you exit the with statement
# Now save the value of filename to your database
