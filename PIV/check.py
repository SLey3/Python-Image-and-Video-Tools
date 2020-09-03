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
            raise InvalidExtention("{extension} is not a supported file extension or is not an extention.".format(extension=file_tuple[1]))
        else:
            logger.log(3, "Image file not found or does not exist.")
            return False
        
def check_video_file(file_path, name, ext) -> bool:
    """
    checks if the file is a video file or if the video exists
    """
    logger = logging.getLogger(__name__)
    if os.path.exists(file_path) and ext in FILE_EXTENSIONS['video']:
        logger.log(0, "File is a Video file and exists.")
        return True
    else:
        file_tuple = (name, ext)
        file_name = name + ext
        if file_tuple[1] in FILE_EXTENSIONS['image'] and os.path.exists(file_path):
            logger.log(1, "File was an Image File.")
            raise ValueError("{name} is not a Video file.".format(name=file_name))
        elif os.path.exists(file_path) and file_tuple[1] not in FILE_EXTENSIONS['video']:
            logger.log(2, "File does exists but the file extension is not recognized.")
            raise InvalidExtention("{extension} is not a supported file extension or is not an extension.".format(extension=file_tuple[1]))
        else:
            logger.log(3, "Video file not found or does not exist.")
            return False