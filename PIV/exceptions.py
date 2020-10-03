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
Exceptions created for the module
"""
import sys
import os
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

class PIVerror(Exception):
    """
    Standard exception
    """
class ImageNotFound(FileNotFoundError):
    """
    Error raised when an Image is not found.
    """
    pass

class VideoNotFound(FileNotFoundError):
    """
    Error raised when a video is not found.
    """
    pass

class InvalidExtention(PIVerror):
    """
    Error raised when incorrect file extension is used.
    """
    pass

class ModuleWarning(Warning):
    """
    Warning raised when a module doesn't meet the required version.
    """
    pass