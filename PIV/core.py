# This is free and unencumbered software released into the public domain.

# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.

# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

# For more information, please refer to <https://unlicense.org>
"""
Heart of the module
"""
from __future__ import absolute_import
import sys
import os
from PIL import Image
import io
import builtins
from pathlib import Path
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from PIV.base import *
from PIV.exceptions import *

class ImageTools:
    """
    Tools for Image modification and data
    """
    def __init__(self):
        self.image = open(image)
        self._size = (0,0)
    @property
    def _width(self):
        """
        Returns the width of Image
        """
        return self._size[0]
    @property
    def _height(self):
        """
        Returns the height of Image
        """
        return self._size[1]
    @property
    def size(self):
        """
        Returns the size of the Image
        """
        return self._size
    def __enter__(self):
        """
        Returns self
        """
        return self
    
    def openImage(image, mode='r'):
        """
        Opens the Image filepath.
        :param image: File path of image
        :param mode: The mode when reading the Image. If presnt, must always be "r"
        """
        if mode != 'r':
            raise ValueError("Bad mode %r" % mode)
        elif isinstance(image, io.StringIO):
            raise ValueError("Image can not be used in StringIO. Binary data must be used.")
        exclusive_image = False
        image_name = ""
        if isinstance(image, Path):
            filename = str(image.resolve())
        #elif isPath(image):
            