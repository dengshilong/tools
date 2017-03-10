import os
import sys
from PIL import Image


for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + "thumbnail.jpg"
    if infile != outfile:
        try:
            im = Image.open(infile)
            size = (im.size[0] / 2, im.size[1] / 2)
            im.thumbnail(size)
            im.save(outfile, "JPEG")
        except IOError:
            print("cannot create thumbnail for", infile)
