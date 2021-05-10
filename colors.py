# Since comments aren't valid in JSON:
# color.json taken from https://github.com/meodai/color-names Copyright (c) 2017 David Aerne

import os
import json
from PIL.ImageColor import getrgb


COLORFILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "colors.json")


with open(COLORFILE) as fh:
    _colors = json.load(fh)

# convert it to an actual dict instead of a weird list
colors = {}
for packed in _colors:
    colors[getrgb(packed["hex"])] = packed["name"]
