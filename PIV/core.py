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
from typing import List
from PIL import Image
from PIL import UnidentifiedImageError
import io
import imghdr
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from PIV.base import *
from PIV.exceptions import *
from PIV.check import *
import PIV.info as info
class ImageTools:
    """
    Tools for Image modification and data
    :param image: these required argument is to initialize the class
    :param perm_save: If true, the PERMS_SAVE list will be used to save paths 
    """
    def __init__(self, image: str, perm_save: bool):
        if check_image_file(image, info.name(image), info.extension(image)):
            self.raw_image = image
            self.image_name = self._name
            PIL_image = Image.open(image, mode='r')
            self.image_ext = '.' + self._format
            self._size = PIL_image.size
            self.perm_save = perm_save
            self.image = self.image_name + self.image_ext
            if perm_save:
                self.path_list = PERM_SAVE
            else:
                self.path_list = TEMP_SAVE
        else:
            raise ImageNotFound("{image_file} either does not exists or cannot be found due to a typo or incorrect filepath.".format(image_file=image))  # noqa: 501

    @property
    def _format(self):
        """
        returns the file extension of the file
        """
        return imghdr.what(self.raw_image)
            
    @property
    def _name(self):
        """
        Returns the name of the file
        """
        name_extension = os.path.basename(self.raw_image)
        return name_extension.rsplit(".", 1)[0]
    
    @property
    def _width(self):
        """
        Returns the width of Image
        """
        return self._size[1]
    
    @property
    def _height(self):
        """
        Returns the height of Image
        """
        return self._size[0]
    
    @property
    def _binary(self):
        bin_data = io.open(self.raw_image, 'rb', buffering=0)
        return bin_data.read()
    
    @property
    def size(self):
        """
        Returns the size of the Image
        """
        return self._size
    
    @staticmethod
    def available_ext() -> List[str]:
        """
        Returns all the currently supported image extensions
        """
        file_list = FILE_EXTENSIONS['image']
        return sorted(file_list)
    
    def _path(self, save=False) -> str:
        """
        Returns the file path of the Image
        :param save: If true, it will save by default into the TEMP_SAVE list or if perm save was enabled, will save the path to the PERM_SAVE list instead
        """  # noqa: E501
        if save:
            self.path_list.append(self.raw_image)
            return self.raw_image
        else:
            return self.raw_image
    
    def convertFile(self, file_extention = "", with_path=False):
        """
        Converts the image's extension
        :param file_extension: The New file extension that would replace the old file extension
        :param with_path: If true, The original image will be declared with its filepath and the new image file will be sent to same path as the orignal
        :param image: created to add the chosen image extension
        """  # noqa: E501
        image_ext = self.image_ext
        image = self.image
        if file_extention in FILE_EXTENSIONS['image']:
            fe = file_extention
        else:
            raise InvalidExtention("{} is not a valid image extention.".format(file_extention))

        if image_ext not in FILE_EXTENSIONS['image']:
            raise InvalidExtention("{} is not a valid image extention.".format(image))   
        if with_path:
            original_path = self._path()
            path_exc = original_path.replace('\\' + image, '')
            print(path_exc)
            os.chdir(path_exc)
            os.rename(image, self.image_name + fe) 
        else:
            os.rename(image, self.image_name + fe) 
        
    def __enter__(self):
        """
        Returns self
        """
        return self
    
    def __repr__(self):
        """
        Returns unambiguous result
        """
        return (f'{self.__class__.__name__}('f'{self.raw_image!r}, {self.perm_save!r})'.format(self=self))