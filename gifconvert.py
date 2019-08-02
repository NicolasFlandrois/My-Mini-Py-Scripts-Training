#!/usr/bin/python3.7
# UTF8
# Date: Thu 11 Jul 2019 11:39:39 CEST
# Author: Nicolas Flandrois
# Description: This script is a simple video converter. Initially intended to
# convert videos into GIF files. See further application to convert in other
# formats with imageio
# Requierments: imageio & imageio-ffmpeg (pip install imageio imageio-ffmpeg)

import imageio
import os


def gifMaker(inputPath, targetFormat):
    outputPath = os.path.splitext(inputPath)[0] + targetFormat
    print(f"converting {inputPath} \n to {outputPath}")
    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()['fps']
    writer = imageio.get_writer(outputPath, fps=fps)
    for frame in reader:
        writer.append_data(frame)
    print(f'Done! \n {inputPath} has been converted to {outputPath}')
    writer.close()


clip = os.path.abspath('pathtovideo.mp4')
gifMaker(clip, '.gif')
