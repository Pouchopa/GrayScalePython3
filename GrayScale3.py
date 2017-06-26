#!/usr/bin/env python
import sys
from shutil import copyfile

param_1= sys.argv[1] 
copyfile(sys.argv[1], 'grayscale.stl')