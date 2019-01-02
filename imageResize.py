"""
Image resize utility by Chris Luginbuhl
Resizes a folder of images to a square size, padding with black pixels.
Usage: imageResize -i (path to folder of images to be resized) -o (path to folder of resized images) -s (final size, in pixels, square) -c (crop mode not yet implemented)
"""

from PIL import Image
import os
from tqdm import tqdm
import argparse
#source path of images, with trailing slash






parser = argparse.ArgumentParser()
parser.add_argument("-i", "--inpath", help="Path to folder of images to be resized")
parser.add_argument("-o", "--outpath", help="Path to folder of resized images (will be created if it doesn't exist)")
parser.add_argument("-s", "--final_size", help="Size in pixels of resized images (square)", type=int)
parser.add_argument("-c", "--cropmode", help="Crop mode, 'f' or 'i' for Fit or fIll", default = 'f')
args = parser.parse_args()

print( "Args {} User {} Password {} size {} ".format(
        args.inpath,
        args.outpath,
        args.final_size,
        args.cropmode
        ))



#path = "/Users/chrisluginbuhl/machine_learning_local/wikiart/Early_Renaissance/facenet/filtered/"

if args.outpath == "":
    args.outpath = os.path.join(args.inpath, "resize")
path = os.path.normpath(args.inpath)
dirs = os.listdir(path)
if args.final_size > 0:
    final_size = args.final_size
else:
    final_size = 64
os.makedirs(os.path.normpath(args.outpath), exist_ok=True)


def resize_aspect_fit():
    index = 0
    for item in dirs:
        print(index)
        if item == '.DS_Store':
            continue
        if os.path.isfile(os.path.join(path, item)):
            im = Image.open(os.path.join(path,item))
            f, e = os.path.splitext(os.path.join(args.outpath, str(index)))
            size = im.size
            ratio = float(final_size) / max(size)
            new_image_size = tuple([int(x*ratio) for x in size])
            im = im.resize(new_image_size, Image.ANTIALIAS)
            new_im = Image.new("RGB", (final_size, final_size))
            new_im.paste(im, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
            new_im.save(f + '.jpg', 'JPEG', quality=70)
            index += 1

print("starting")
resize_aspect_fit()
