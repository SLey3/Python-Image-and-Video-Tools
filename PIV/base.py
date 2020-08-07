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
base variable definitions
"""
from __future__ import absolute_import
import sys
import os
import re
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

FILE_EXTENSIONS = {
    'image':[
        '.jpg',
        '.jpeg',
        '.jpe',
        '.jif',
        '.jfif',
        '.jfi',
        '.png',
        '.ico',
        '.gif',
        '.tiff',
        '.tif',
        '.psd',
        '.pdf',
        '.eps',
        '.ai',
        '.indd',
        '.ind',
        '.indt',
        '.raw',
        '.arw',
        '.cr2',
        '.nrw',
        '.k25',
        '.crw',
        '.nef',
        '.pef',
        '.webp',
        '.bmp',
        '.dib',
        '.heif',
        '.heic',
        '.jp2',
        '.j2k',
        '.jpf',
        '.jpx',
        '.jpm',
        '.mj2',
        '.svg',
        '.svgz',
        '.eps'
    ],
    'video':[
        '.mp2',
        '.mp3',
        '.mp4',
        '.m4p',
        '.m4v',
        '.webm',
        '.mpg',
        '.mpeg',
        '.mpe',
        '.mpv',
        '.ogg',
        '.avi',
        '.wmv',
        '.mov',
        '.qt',
        '.flv',
        '.swf',
        '.avchd'
    ]
}
READONLY = 0

OPEN = {}

SAVE = {}