#  Copyright 2020 Sergio Ley Languren

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
"""
Heart of the module
"""
from __future__ import absolute_import
import sys
import os
import glob
import shutil
import threading
from typing import List
from typing import Any
from PIL import Image
from PIL import UnidentifiedImageError
import io
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
    def __init__(self, image: image_name_util, perm_save: bool) -> Any:
        if check_image_file(image, info.name(image), info.extension(image)):
            self.raw_image = image
            self.image_name = self._name
            self.PIL_image = Image.open(image, mode='r')
            self.image_ext = '.' + self._format
            self._size = self.PIL_image.size
            self.perm_save = perm_save
            self.image = info.name(image) + info.extension(image)
            self.fp_regex = PATH_REGEX
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
        filename = os.path.basename(self.raw_image)
        image_extension = os.path.splitext(filename)
        return image_extension[1]
            
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
        """
        Returns the binary data of the Image
        """
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
        Returns all the currently supported 
        image extensions
        """
        # Bug: 2 list copies made when 1 is supposed to be returned
        return sorted(FILE_EXTENSIONS['image'])
    
    def path(self, save: bool = False) -> str:
        """
        Returns the file path of the Image
        :param save: If true, it will save by default into the TEMP_SAVE list or if perm save was enabled, will save the path to the PERM_SAVE list instead
        """  # noqa: E501
        if self.fp_regex.match(self.raw_image):
            if save:
                self.path_list.append(self.raw_image)
                return self.raw_image
            else:
                return self.raw_image
        else:
            path = ""
            directory = os.path.abspath('.')
            for file in glob.glob('*' + self._format):
                if self.raw_image == file:
                    path = os.path.normpath(os.path.join(directory, file))
                    if save:
                        self.path_list.append(path)
                    return path
                else:
                    os.chdir('..')
                    directory = os.path.abspath('.')
                    fp_found = False
                    path = ""
                    while fp_found != True:  # noqa: E712
                        for file in glob.glob('*' + self._format):
                            if file == self.raw_image:
                                path = os.path.normpath(os.path.join(directory, file))
                            else:
                                path = ""
                        if os.path.isfile(path):
                            if save:
                                self.path_list.append(path)
                                fp_found = True
                            else:
                                fp_found = True
                        else:
                            os.chdir('..')
                            directory = os.path.abspath('.')
                    return path
                
    def convertFile(self, file_extention: str = "", file_dest: str = "", keep_old: bool = False): # noqa: E252
        """
        Converts the image's extension
        :param file_extension: The New file extension that would replace the old file extension
        :param file_dest: The new file that replaced the old file extension would be moved to the folder specified
        :param keep_old: If True, then the old file will not be deleted
        """  # noqa: E501
        if file_extention in FILE_EXTENSIONS['image']:
            fe = file_extention
        elif file_extention in FILE_EXTENSIONS['video']:
            raise ValueError("""{ext} is a video extension. Please use an Image extension. Check documentation for 
                             supported Image extenions""".format(ext=file_extention))
        else:
            raise InvalidExtention("{} is not a valid image extention.".format(file_extention))
        
        path, _path = (self.path(), self.path().rsplit('.', 1)[0])
        self.PIL_image.close()
        if keep_old:
            shutil.copy(path, _path + '_original' + fe)
            # src = path
            # dest = _path + '_original' + fe
            # threading.Thread(target=shutil.copy, args=[src, dest]).start() # noq: E241
        os.rename(path,  _path + fe) 
        image_name_util(_path + fe)
        if len(file_dest) > 0:
            shutil.move(_path + fe, file_dest)
        self.PIL_image = Image.open(_path + fe, mode='r')
    
    def close(self):
        """
        Closes the ImageTools class
        """
        if self.path_list == TEMP_SAVE:
            self.path_list.clear()
            
        del self.path_list
        self.PIL_image.close()
            
    def __enter__(self):
        """
        Returns self
        """
        return self
    
    def __exit__(self, type, value, traceback):
        """
        Exits self
        """
        self.close()
    
    def __repr__(self):
        """
        Returns unambiguous result
        """
        return (f'{self.__class__.__name__}('f'{self.raw_image!r}, {self.perm_save!r})'.format(self=self))