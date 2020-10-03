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
Necessary checks for the module
"""
from PIV.base import FILE_EXTENSIONS
from PIV.exceptions import InvalidExtention
import os
import logging

def check_image_file(file_path, name, ext) -> bool:
    """
    checks if the file is an image file or if the image file exists
    """
    logger = logging.getLogger(__name__)
    if os.path.exists(file_path) and ext in FILE_EXTENSIONS['image']:
        logger.log(0, "File is an Image file and exists.")
        return True
    else:
        file_tuple = (name, ext)
        file_name = name + ext
        if file_tuple[1] in FILE_EXTENSIONS['video'] and os.path.exists(file_path):
            logger.log(1, "File was a Video File.")
            raise ValueError("{name} is not an Image file.".format(name=file_name))
        elif os.path.exists(file_path) and file_tuple[1] not in FILE_EXTENSIONS['image']:
            logger.log(2, "File does exist but the file extension is not recognised.")
            raise InvalidExtention("{extension} is not a supported file extension or is not an extention.".format(extension=file_tuple[1])) # noqa: E501
        else:
            logger.log(3, "Image file not found or does not exist.")
            return False
        
# def check_video_file(file_path, name, ext) -> bool:
#     """
#     checks if the file is a video file or if the video exists
#     """
#     logger = logging.getLogger(__name__)
#     if os.path.exists(file_path) and ext in FILE_EXTENSIONS['video']:
#         logger.log(0, "File is a Video file and exists.")
#         return True
#     else:
#         file_tuple = (name, ext)
#         file_name = name + ext
#         if file_tuple[1] in FILE_EXTENSIONS['image'] and os.path.exists(file_path):
#             logger.log(1, "File was an Image File.")
#             raise ValueError("{name} is not a Video file.".format(name=file_name))
#         elif os.path.exists(file_path) and file_tuple[1] not in FILE_EXTENSIONS['video']:
#             logger.log(2, "File does exists but the file extension is not recognized.")
#             raise InvalidExtention("{extension} is not a supported file extension or is not an extension.".format(extension=file_tuple[1]))  # noqa: E501
#         else:
#             logger.log(3, "Video file not found or does not exist.")
#             return False