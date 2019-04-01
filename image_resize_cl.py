"""
Chris Luginbuhl Apr 2019
Resizes images to square .jpg for training GANs, padding with black.
"""


from PIL import Image
import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--inpath", help="Path to folder of images to resize", default = None)
parser.add_argument("-o", "--outpath", help="Path to folder of resized images (will be created if it doesn't exist), default = args.category", default = None)
parser.add_argument("-s", "--finalsize", help="Size in pixels of resized images (square)", default = 128, type=int)
parser.add_argument("-n", "--makenumbered", help="change filenames to numbered series", dest='makenumbered', default=False, action='store_true')
parser.add_argument("-u", "--suffix", help = "Add suffix to filename if not making files numbered", default = "")
args = parser.parse_args()

print()
print( "Input Path {}, Output Path {}, Final Size {}, Make Numbered{}, Suffix {}".format(
        args.inpath,
        args.outpath,
        args.finalsize,
        args.makenumbered,
        args.suffix
        ))
print()

inPath = os.path.normpath(args.inpath)
outPath = os.path.normpath(args.outpath)

dirs = os.listdir(inPath)
os.makedirs(os.path.join(outPath), exist_ok=True)

def resize_aspect_fit():
    index = 0
    for item in dirs:
        print(index)
        if item == '.DS_Store':
            continue
        elif os.path.isfile(os.path.join(inPath, item)):
            im = Image.open(os.path.join(inPath, item))
            if args.makenumbered:
                f, e = os.path.splitext(os.path.join(outPath, str(index)))
            else:
                f, e = os.path.splitext(os.path.join(outPath, item))
            size = im.size
            ratio = float(args.finalsize) / max(size)   # the resize arithmetic is a little roundabout, but works
            new_image_size = tuple([int(x*ratio) for x in size])
            im = im.resize(new_image_size, Image.ANTIALIAS)
            new_im = Image.new("RGB", (args.finalsize, args.finalsize))
            new_im.paste(im, ((args.finalsize-new_image_size[0])//2, (args.finalsize-new_image_size[1])//2))
            new_im.save(f + args.suffix + '.jpg', 'JPEG', quality=70)
            index += 1

print("starting")
resize_aspect_fit()
