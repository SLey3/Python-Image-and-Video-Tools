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
import sys
import os
import glob
import shutil
import io
import matplotlib.pyplot as plt
import numpy as np
from typing import List
from typing import Any
from typing import Optional
from typing import Tuple
from PIL import Image
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
    def __init__(self, image: str, perm_save: bool) -> Any:
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
        Converts the image's extension to the desired extension.
        :param file_extension: The New file extension that would replace the old file extension
        :param file_dest: The new file that replaced the old file extension would be moved to the folder specified
        :param keep_old: If True, then the old file will not be deleted
        """  # noqa: E501
        if file_extention in FILE_EXTENSIONS['image']:
            fe = file_extention
            name = self._name
        elif file_extention in FILE_EXTENSIONS['video']:
            raise ValueError("""{ext} is a video extension. Please use an Image extension. Check documentation for 
                             supported Image extenions""".format(ext=file_extention))
        else:
            raise InvalidExtention("{} is not a valid image extention.".format(file_extention))
        
        path, _path = (self.path(), self.path().rsplit('.', 1)[0])
        self.PIL_image.close()
        if keep_old:
            os.mkdir(_path.replace(name, '') + 'original_image')
            copy_path = _path.replace(name, '') + '\\original_image\\{name}_original{ext}'.format(name=self._name, ext=self._format) # noqa: E501
            shutil.copy(path, copy_path, follow_symlinks=True)
        os.rename(path, _path + fe)
        os.rename(path + fe, _path + fe)
        self.__init__(_path + fe, self.perm_save)
        self.PIL_image.close()
        if len(file_dest) != 0: # noqa: F632
            shutil.move(_path + fe, file_dest)
        self.PIL_image = Image.open(_path + fe, mode='r')
        
    @staticmethod
    def graph(x_length: List[int] = [], y_length: List[int] = [], points: List[List[Tuple[int, int]]] = [],
              title: Optional[str] = None, image_extension: str = ".jpeg",
              image_name: str = "",
              x_title: Optional[str] = None, y_title: Optional[str] = None,
              include_legend: bool = False,
              labels: List[str] = [], with_linspace: bool = False,
              lin_start: Optional[int] = None, lin_end: Optional[int] = None,
              lin_num: Optional[int] = None, lin_linear: bool = True,
              lin_quadratic: bool = False, lin_cubic: bool = False
              ):
        """
        Creates an Image that contains the created graph. 
        :param x_length: The minimum and maximum length for the x axis
        :param y_length: THe minimum and maximum length for the y axis
        :param points: List of tuples that contains x and y coordinates
        :param title: Title of the Graph
        :param image_extension: The extension for the Graph Image. The default is .jpeg
        :param image_name: Name of the Graphs image
        :param x_title: The subtitle for the x axis
        :param y_title: The subtitle for the y axis
        :param include_legend: This would include the graphs legend. Default Value is False
        :param labels: The labels for the graphs lines. This can be also used if :param multiple_points:
        is in its Default value. Only set labels if :param include_legend: is set to True.
        :param with_linspace: If set to true, Don't set any points for :param points: as the graph will depend
        on `np.linspace` for the graphs lines.
        :param lin_start: The starting value of the linspace sequence
        :param lin_end: The end value of the linspace sequence
        :param lin_num: The number of samples to generate. The default is 50.
        :param lin_linear: If true, the Linear line in the graph is based on linspace. Default is True.
        :param lin_quadratic: If true of Quadratic lines in the graph is based on linspace
        :param lin_cubic: If true of Cubic lines in the graph is based on linspace
        For more information on how to use this function, go to the documention.
        """
        if with_linspace:
            x = np.linspace(lin_start, lin_end, num=lin_num if not None else 50)
            if len(labels) > 3:
                raise IndexError("The value of labels must not exceed 3 in order to use linspace.")
            if lin_linear:
                plt.plot(x, x, label=labels.pop(0))
            if lin_quadratic:
                plt.plot(x, x**2, label=labels.pop(0))
            if lin_cubic:
                plt.plot(x, x**3, label=labels.pop(0))
            if title is not None:
                plt.title(title)
            if x_title is not None:
                plt.xlabel(x_title)
            if y_title is not None:
                plt.ylabel(y_title)
            if include_legend:
                plt.legend()
            if image_extension not in FILE_EXTENSIONS['image']:
                raise InvalidExtention(
                    "{ext} is not a valid file extention or is currently not supported by PIV.".format(
                        ext=image_extension))
            plt.savefig("{img_name}{ext}".format(img_name=image_name, ext=image_extension))
        else:
            plt.xlim(x_length[0], x_length[1])
            plt.ylim(y_length[0], y_length[1])
            for line in points:
                x = [x_point[0] for x_point in line]
                y = [y_point[1] for y_point in line]
                plt.plot(x, y, label=labels.pop(0))
            if image_extension not in FILE_EXTENSIONS['image']:
                raise InvalidExtention(
                    "{ext} is not a valid file extention or is currently not supported by PIV.".format(
                        ext=image_extension))
            if include_legend:
                plt.legend()
            plt.savefig("{img_name}{ext}".format(img_name=image_name, ext=image_extension))
    
    def close(self):
        """
        Closes the ImageTools class
        """
        if self.path_list == TEMP_SAVE:
            self.path_list.clear()
        self.PIL_image.close()
        del self
            
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