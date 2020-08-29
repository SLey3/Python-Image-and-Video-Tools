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
import sys
import os

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
        '.eps',
        '.img'
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

TEMP_SAVE = []

PATH_ENTRIES = []

PERM_SAVE = []

# for testing
BINARY = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xff\xdb\x00\x84\x00\t\x06\x07\x13\x13\x12\x12\x12\x13\x12\x15\x15\x12\x15\x12\x15\x10\x10\x15\x15\x17\x10\x10\x10\x0f\x10\x15\x15\x16\x16\x15\x15\x15\x15\x18\x1d( \x18\x1a%\x1b\x15\x15!1!%)+...\x17\x1f383,7(-.+\x01\n\n\n\x0e\r\x0e\x1a\x10\x10\x17-\x1d\x1d\x1f-------------/---+------+-++---------+-------+-+-+\xff\xc0\x00\x11\x08\x00\xc9\x00\xfb\x03\x01"\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x1b\x00\x00\x02\x03\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x05\x02\x03\x06\x01\x00\x07\xff\xc4\x00@\x10\x00\x01\x03\x03\x03\x02\x04\x04\x03\x05\x05\x07\x05\x00\x00\x00\x01\x00\x02\x11\x03\x04!\x05\x121AQ\x06\x13"a2q\x81\x91B\xa1\xb1\x14#R\xc1\xd1b\x92\xb2\xe1\xf0\x153rt\x82\xc2\xf1\x074Cs\xb3\xff\xc4\x00\x19\x01\x00\x03\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\xff\xc4\x00(\x11\x00\x02\x02\x02\x02\x01\x03\x03\x05\x01\x00\x00\x00\x00\x00\x00\x00\x01\x02\x11\x03!\x121A\x13"Q\x04q\x912Ba\xa1\xe1\x05\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00?\x00\xfbH\xa8\x14]X$\xa2\xe4\x8c(U\xa8rd\xa4\xd3\x18\xf8<\x15\xd2\xb3\xd6\x9a\x83\x81\x82\x9cR\xba\x05\x14\x05\xae\n\x05\xaa\xcd\xc1w\t\x0c\xa8\x05\xed\xaa\xc2\xaa}D\x01\xed\xab\x9bT\x04\x95{Z\x81\x15\x86)mS+\x88\x02\xb2\xa0B\xb8\x85\x12\x13\x02\xa5\xc5a\n;P\x04Wa\x01\xa9VsG\xa4J\xae\x95\xd5H\x12\x12\xb0\xa1\x9c!\xea\xdc\x00ay\x8eq\n\x91k.\x92\x8b\n\x08\x99\nt\xe8\xc2\xb1\x8d\x01F\xa3\xc2,\x08\xb9\xa1*\xb9\xbek]\x011{\xd2\xe7\xe9\xc0\xbbrh\x0b\xa9V\x95i\n\xbaM\x01N\xa5EB"\xe7\xaa\x85E\r\xcalrC.kWE0\xbc\x1e\xaa\xabU1\x04\xb5\x8a^@B\xd1\xbaDy\xe8\x02\x87\xd2^\xda\xacc\xe5sj\x91\x95>\x88\x19P\x15;\x15:\xe6p\x85\xa8\xc8T\x84\xc2\x7fkp\xea\xae\xa7|R\xdd\xeb\xd4\xaa\x84\xe8V7\x17e[F\xb0(\x00p\xa5mOs\x87e,hn\x1c\x17\x83\xe5r\xa8\x00*\x03\xc3TYT\x12J\xe0\xa8\x15\x15n\xc6\xd9A\xd1\xbb\x04\x94X\xe8j\x1c\x17\x9c\x80\xa5P\xca"\xa5X\x08\xb0\xa3\xa5\xea\x0ez\x0e\xe2\xb9\x02a\tF\xf8\xbc\x90\x12\xecc\\\x15s)\x8e\xca\x8ax\x19V\xb1\xe9\x92z\xaf\xb2\xa1\xa5r\xe2\xe4\x04%Z\xf20\x80\x05\xd7\xf5\xc6\xd0a3\xc0Y\xbd\x1b\xc5f\xab\xf3\x84^\xa5\xe1\xc3q;\xdc`\xa1\xb4\xef\t2\x83\xb7I1\xddZ\xaa\xd8\x9d\x9a\x91u!HW\x94\xa6\xf3R\xa7M\xb9 BL\xdf\x12\x82Lq\xdd:\x15\x9a\xb7T\x1d\xd4Mq\xdd!\xb7\xbb5D\x87"\xac\x98d\xe6Q@1\xa8\xec*i\xd4*\xd2\xf1\n\xa7\xd4\xec\x8a\x02\xd1]L=\x02Ld\xa9\xdb_5\xc6\x01\x08\xa0\x0bp\x12\xa7\xbdE\xd0\x85ua<\xa0\x07\x9eH\x08w\xc8D\x07.m\x05H\xc0_QQU\xd2\x8c\xb8\xb7\x08B!Z\x13\x04r\xa87(\xef.P\xf7\x0c\x8c\xa6 \xcbQ\xc4\xa6\x8c{Z\xb3\xf6\xceq\xe16\xb5\xa0z\xac\xe4Z\t5w\x1c\xf0\xa5Q\xa0\xaa\x9e\xc0\xb8\xc7@SC\xb3\xcfh\x02\x10\x84\x80p\xba\xe7\xb9\xc6\x07\x0b\xaf\xb5\x81\x94P\x16\xd2\xb8\x01^\xda\x9b\x92\xa7\xc0D\xda]\x88\x84\xa8,\xf6\xa5v\x07\xa7\xa9\xc2\x8d\xa8\x14\xdb1\x1dJ\xe3m7\xbfy\xe8\xbb\xac?m2\x00\xe8\x98\t\xaax\x94:\xa9\xa6\xde\x9c\x9e\xc9\xcd\xbd\xc9\x89_3\xabn\xf68\xd6\x06\t$\xa7\xb6\x1e#\xfd\xdf\xa8\xe62\xb4\xe1\xf0G!\xc6\xbb\xa8\xed\xc98^\xd1o7\x89\x1c,N\xad\xab:\xb1-h\xe7\x12\x9d\xe8W\x1eU8)\xf0\xd0\xb9li\xacx\x8f\xc8sA\xeaR\xad_\xc5R\xcfO\'\x88K\xb5\xabG\xdc?sD\xc7\n\xfd;\xc3\xae\xd8\x0b\xbe\xaa\x94R\xecNL\xcc\xd5\xba{\xdd.&\t\xcan\xeb\x8aa\x909\xe8\xa9\xd54\xed\x84\xc7C\t\x97\x874 \xff\x00[\xb3\xdb\xb2\xb7TB\xb1M\x96\xa4\xfad\x8c\xc1\xe1j\xb4\x0b\xe7?$\x14m]\x12\x90\xe4\x04\xc7O\xb0`\xf8T6\x8bI\x81\xd4\xbd\rv\xd2\x991\x80\xe4 5\x1d!\xae{]\xd4\x19E\xbe\xe5\xb4\xdb\x93\xc2\x91\x8b\xf5\xe7\x96\xb0\xc7+1\xa2\n\x81\xe5\xee(\xaf\x10\xea\xe1\xc4\x01\x9c\xe5(\xff\x00i\x91\xc0\x85\xa2Z!\xbd\x8f/\xfcBX\xed\xa9MO\x10>Lp\x96\xd7%\xc6O*\xbd\x8a\x94P\x9c\x99\xf6\xb7\x15\xc6=\x08\xe7\x99W\xb1\x92\xb9\x8d\x8e\xd6|\xe1\x03p!1\xf2!\x01v\xc5HL\x85\x13\x84%\xcb\xc90\x88uH\n\x16\xb92S\x10\xc7M\xa3\x03(\x9a\xd5@\xc2\x1d\xb7\x00a\x0c\xfa\xb2\xe5\x99t\x1dY\xa6\x12\xca\xb5\x9c\x01\x94\xd1\x8e\x90\x80\xbe\x8f\x85\x00U\xa6\xdf\x83*7w\xaf&"\x02\xb2\xda\xd5\xb4\xc4\x8e\xaa\xba\x8e\x0e\x9c\xa0\n<\xd5\xcaus\xca\x91\r\x03\x94\xaa\xe2\xe5\xad%\xc5\xc06~ps\xdb\xe4S\xa05,\xb8\x00a,\xd65\x16\x86\x12OD\xae\x9e\xb9H\x80<\xd6\xc9\xc0\x9d\xc2~\xe1"\xd5/\x9a\xf7\x16\x9a\x8d\r\x1d$\xc9N)ybw\xe1\x03\x9b\x83U\xc1\xa7\r\xec\xaa\xbc\xb4\x02#\xaa\xf3.\xe8\x0f\xfeQ\xf3\x87g\xe5\x8c\xa3i\xdd\xd01\xfb\xd6\x1f\xaf\xf5[\xa7\x1f\x0c\xc5\xa9yB\xdbZP\xe1(\xedE\xe4\x80\x1b\xcc\xf4L\x8d\xb5*\x8d\x969\xa4wi\x06\x0f\xd1\x1dOOc\x1a\x1e\x7f\x0ee7$\x95\xb0Qm\xd1\x1a7\xf4\xed(5\xf5\xf0\xe20\xd1\x97\xbb\xe4\x12+\xbf\x1f\xbav\xd3\xa6\xc0x\xd8\xed\xces}\xdc[\xc7\xdb\xea\x84\xd7n\xda\xf79\xef\xa8\xe9nv\x12Z\x07`\x03ct\xc7\x05&\xb3\xbai$\x96\x9d\xa6Hl\x9am\xe7\xf0\x9c\xed\\^\xab\x96\xce\xbfIGC\'k5*:_M\x8f\xea\xed\x8f\r#\xfe\x97ei\xb4\x9f\x14\xd0\x000\xb1\xf4\xccD\x10\x0f\x1c\xf0\xb2\x15h5\xcd%\x92\x1c\xd9\xdc\x1d\x1b\x83f3\x1f\xa8\x9f\xa2\x9bh\xb5\xcc\x9e\x1d\xeew1\xe3\x1c8`\x7f\x97\t\xfa\x92\x0fN&\xbbR\xd5\xd8\xec6\xabA<n;g\xe4O)\x9e\x95}\xb5\xa3q\xcc}\xd7\xcdjU\x00yu\x07\xa6dn\x98\x93\x8f\x8b\x96\x91#\xe9\x9c\xa1\xff\x00o}\x07\xed\xa1S\xcc\xc4\xbe\x8b\x8c\x12?\xb0p\t\x1e\xc0\x1e\xea\xe3\x92\xf4\xc8\x96:\xda7z\xd7\x88\x1d\xbe\x19\xc0\xe5&\xbd\xd4\x9fPA(}>\xe9\x95\xdb\xbd\x93\xfd\xa0p\xe6\x9e\xc5Z\xfbs\x85\xd2\x92\xf0s\xb6\xca\x00\x11\x95\x01JQ\x95,\\\x04\xa3t\xed,\xb9\xb2S&\x84de^\xd8Dj\x16\xe1\xa4\x84\x1a`}\xa1\xd4@\n\xb0\xd8J\xf5M}\xa3\r\xcf\xc9.\xa1\xe2V\x93\x13\x1f5\xc5\xb6u\x1a:\x970\x12\xab\xea\xe5)\xbe\xf1#\x01\x89\xc7\xb2\x0e\xbe\xba\xd7D\x15j,\x96\xd0\xe1\xf5p\xa3mP\xcaHu\x11\xdf\x08+\xbdq\xc0\xc3\x04\xaa\xa6\xc2\xd26\xa0\x8e\xa5L\xd5cs+\x03c{Z\xb5NH\x01;\xadA\xf8\xca\x9e\x03R5\x07UcZL\x80\x02\xcf[^\x1a\xf5\xe4\x18`?t\xae\xee\xdd\xd12\x96\xdb\xeaf\x9b\x88\t\xa8\t\xca\x8f\xa0\xeau\xc3Y\xcf\xd9e\xaeuM\xb9\xdc\x00\x9d\xbd\xc9>\xc3\xed\xf7J\xaajuj\x11\'\xe4\x93\xeb\xb7\xeda,/\rpd\xb4\x9c\x8d\xddCH\x12\x1d?\xf9S\x92\xe0\xbf\x96V:\x93\x18]\xeb\xb5\x1d0\x0bGO\xe2$\x11\xcf\xe9\x88\xcc\xa4\x8d\xd4\x081\xd4:f&g\x19=b\'\xea\x94U\xd5\x1f\xb6\x1b;\xb6\x80`\x1d\xcf O\xf5([f\xd6~\xe8xc\xc1\xc8s\x88qi\x18\x81\x07\x1c,\xbe\xe6\x9fcCOQ\xeaL8\x1d\xa6O=d\xfd:\xfc\xfe\x9e7[\x863\xdf\xa6Gx\xe4\xf0\xb2\xd5\xeb\xdc\xd3vD\x81\xc9i\xdc1\xc4\xf7M4\xcb\xd7<Hl8\xe0\xc8\x06]8\xc7H\x11\xdf\xf4\x8a\x15\x97\xd4\xa7&\x04\xcfYSn\x94q\xb9\xdfA\x84U\nE\xc7\x04@\xf8\x9cx\xf7\x9e\xe7(\xf3^\x95\x10\x0c\x07\x98$\x93\x11#\x11\x113\xf2N\xe8*\xc1\xf4\xa6\x9a.\xdc\xc2\xe1\x1c\x83;\\=\xfb\xadi\xd6Xi\x99.n\xe1\xb4q\xc9\x13 \xf1\x03\xba\xce\xbf\xc4\x046@\r\xc6\xe1$z\xa701"$\x1f\xf5\x08\x03s\xe6\x10\xe78\x96\xc6v\xf3\x898&\x7f<\xe1)M\xf1hj\n\xd3*\xd7\x18\x1a\xe69\xb9%\xa0\xbc\xef\xdc\x1cg\xa4@\x00\x88\xe7\xe6\x84\xa1r\xc0A.\xdd<\xb7\x03h\x100~\xff\x00d\x8bW\xac\xf3&\x94\xec\x07\x99\xc3\xf9\x92\x01\xfc\xd2v\xdc\xberx\xe3\x8f\xb1\xee\x94b\xe8\x99Kf\xee\xa5P\xd2\xd82\xeebAo8\x1f9L\x9b\xb5\xa0\x01Q\xed\xeb\x1bD,\x03\xde\xed\xac\xa8\xd2\';\xc6p\xe0\xe3\x07\xf2\x05X\xcf\x11\xd7\x99\xdf$\xe3?\xeb\x94\xea\xc3\x95\x1b\xdb\x9a\xd4\xeaS,$\x12d\x19l\x074\xf4=\xba\xfd\xd2\x83\xe1\xf7\xedv\xdf[c\xf7m\'\xf7\x94\x9f\xd0\xb0\x83${eg\x7f\xdau\xea\xbfh\x92H\xf4\x86\xc0\x98\xf7O?d\xa8\xea\x11V\xa6\xc7\x02\r32i\xbf\x81\xba2\xde\x9ftU\x07+\x16\xd5\xbd\xb9\xa4\xf6\x92H|\x90^8\xa8g\x1b\x87\x07\xa8\x82\x01_D\xf0\xf5\xf9\xadI\xaf{Z\x1e\x002\xdc\xb1\xe0\xf0G\xdb!|\xfd\x9a\x9dr]N\xbd\'T,\x89{\x04\xd4\x00\xfc$\xc0\x87\xb7\x9eV\xbf\xc3\xe1\xac\xb7hd\x80rw\x074\xcf\xfc\'\x85\xb64\xec\xc6mP\xf2\xfa\xf0D*\xe8k\x05\xad\x88\xcc%\xf5J\xa4\xb5tQ\x8d\x84\xb5\xc6\xab\xbd\xca,\xe8\xeeTi\xac-!\xd1\x84\xd4\xea\x83\xb2O\xf8\x1f\xdcWc\xa8\xf3\xbaI\x92~\xe8\x0b\xab\x82\\H\xee\xbb\x19\x85/\xd9K\x88\x00(\xa4U\xb1\xae\x85d\xda\x8d%\xd9>\xe9V\xa9OeR\x1a\xb4\xba\x1e\x9c\xe64\xfb\xe5)\xd7,\x9d\xe6\x12D\x04Z\xb1\xb4\xe8\x1bJ\xa6j:\t\xc7%9\xafJ\x9d1\x98\x93\xc2CoP\xb0\xc8\xf9(]Ws\xcc\x9f\xa2*\xc5at/\x83\x1eH\xc2.\xa6\xb6II\xdbA]N\x9a\x1a@\x9b\x1bW\xd4\xe5\x9cg\xa2L\x1b&OtC\x19%\x15SMtHB\x07\xb2\xebJ \xc4,\xc7\x8c\xb4\x90\xd3\xe7|M$\x87\x0f\xc4\xc2s \xf5\x12\x0e?\xd0\xd6Z\xda\x96\x89^u\xa3\xaapp\x94\xa0\xa5\xd8\xe3>\'\xc7\xfc\xc2\xd3"}\xb9\x83\xee\x17\x9bY\xc1\xdb\xe71\x18$\x12\n\xfa\xb5m\x13w\xa1\xd4\xc3\xfa\x86\x86\xc9\x1e\xe28U;\xc0\x14\x1c\xdd\xf5H\xa0\xd9\xe0\x10j:=\x8e\x1a?\xd4,\'\x15\x1f(\xda\x12r\xf0|\xe6\xd6\xe1\xe4\x16n\xe7\xb8\x9f\xbau\xe1}\x16\xb5J\x9bv?p\xc3ZD4\x97G\xaaO\x00\x0f\xe5\xee\xb6\xb6\x9e\x1e\xd2i\xbbh\xfd\xeb\x9b\x97\x13R\xa3\x83{n\xd9\r\x9fhZk\x1b\xcbj`\x8aA\x8c\xdd\xce\xd0\x03\x9d\xf3<\x95\x9a\xdfE\xf5\xd8\x9e\xa7\x83\xd9\xb5\x81\xd5\x0e\x19\xb4\xb6\x98\xc3\x9e\\\xe3\xbc\x93\xecGH\xc2\xc6\xeb\x9aK\xa8<\x9a\x90i\x8f\xf7~\xb8.\x9e\x91\x18<t\x00\xaf\xa9\xd4\xb9oI\xcf\xcc\xa0o6\xb8m%\xb9\xe8G\xf9\'A\xc8\xf8\xab\xab\x078`\xb5\x93\xf5\x98\x03\'\xf3E2\xb3\xbc\xb71\xa7\x93\xd3\xbc\xf1\xd8-G\x8a|7\x0co\x97M\xa008\x88-\x00\xb9\xc5\xa5\xc6\x06K\xa1\xa38\x00\x03\xed\x18\x8b\xa2i\xfadO\'\xa0\x07\'\x1d\xfa*hJF\x92\xfa\xd5\xae\xaa\xcb{|\xb06\x08\xc1;@\xcb\x9cx9\xc9Y\xddcA\x14\xda\xf7\xf7yhp\x83L4\xc4G^\xe9\x9f\x86uF\xd0\xaa+:Ix,\xe6\x03\x01\xc13\xd4\xf3\x8e\x13MF\xe5\xb5\x9a\xfaa\xbe\x82\xf9i\xe0\xf0\x0e\x07O\xfc\xa9Z\x1b\xf7\t\xbc*m\xea\xb1\xb4\xab06\xa52\xe65\xe4\xede]\xf3\x12x\xdd\x93\x13\xcf\xe4\x93x\x8b\xc3O\xb6!\xd9}"\x07\xaa\x08\xda\xfe\xa0\xf6\x07\xa2\xac\xb0\xb1\xe5\xa7\xe1>\x97\x03\xf0\x91\xef\xef\xee\xb4\xda5\xadGQ\xf2\xeb\xb9\xfeApqk\xa6KpG9#\x01kz\xe8\xc6\x8c\x9e\x9e\x1a\x1c\tq\x88\xc0\x923\xf3N.n\xe9\x18vAx{*d\xed\x92\x00i#\xf8B\xbf\xc4^\x1f\xa4\xc7\x97P>\x83\xea\r\xcc\xd3\xc4\x91\x9fyY{\x96\xc1\x83\xc8\xfaJ\x8a\xb6U\xd26\xbe\t\xa5Ty\x8f$\x1aq\xb0N^\x1c\xd2\x08\xfd\\>\x8bO\xca\xc6\xf8\x12\xfb\xd6\xeaD\xf2\xd2\xe6\x8e\xee\x1bw}v\x86\xfd\x8a\xd9\xb5t\xe3z1\x9a\xd9\xc7\xb5P\\\xae\xaa\xe5Aj\xd5\x19\xb0\xea7b\x00\xfa*\xbc\x94\x13\xa5p\\\xbb\xba\x12\x0b4\x16z\t0J\xd0\xe9z\x08\xe4\xe1J\x8b\xf6\xb2}\x95G\xc4\x81\x98\x02J\xe3\xb93\xae\xa2\x90\xce\xe86\x90\xf6Y\rkPk\xc9\r\xfb\xa9jz\xb3\xebs\x80\x96yj\xa2\xab\xb2%+\xe8\x11\xcdV\xd1\xa2\xafu0\x14\r@\x16\x96gE\xce\xb71\xc2\xa1\xcd\x84So\x86\xd8@\xd5r\x12~G&\xbc\x16\xd0\xa8\x03\x81+@\xcdE\xa5\x91\x89Yw7\x0b\xact-\x14H\xe49\xadp\xe7Ho\n\xdd&\xec\x875\x87\xf1\x10\xdc\xf4$\xc2\xabN\xac\x032\x87\xa4&\xa6\xe1\x88;\x87\xb1\x19\tI:t\t\xeco\x7f\xab\ts \x96|%\xad\x90H\xe2I\x1d}\xd57w4^6\xb8<\x80\x00\x02ZO\xd7q\x9f\xa9I5*-/.-\x12\\]\x07\xd4\x06g\xaa\xe5\x9d\xb3\\sN\x9b\xbd\x8bG\xea \xfek\xc7\xc1\xff\x003,W)N\xe4z\x19>\xb2\r\xf1Q\xa49\xb0\xd3\xe808\x8an\x87\x1d\xe7q`l\x98\x81\x93\x9e\x07\x1d\x94\xaej\xb3\x8f,OL\x02\xdf\xa9C\xb6\xc2\x91\x07l\xb1\xd1\x86\x98-\xfa8\xff\x008J\xee)Uf];f\x01\xe9\xf9\x15\xd3\x18\xf0\xd33o\x96\xd0\xf9\x97\x87\x82@\xc7$\x88\x9f\xa1R\xa9r\xfcm\r>\xe0\x96\x9f\xe6\xb3\x94\xee\x1f\xf8\x0c\xfbzs\xf7+\xc7Ps]\xfb\xcadG]\xa1\xd2?\xe9TH\xee\xee\xf9\xfba\xb4K\xeaG\xa6\x0cA\xee\\\x7f\xa2\xf9.\xbbl\xf6Vp\xaa\x1b\xbf\x06\x1a\xe6\xb9\xac\x1d\xa2I\x1f\\\x9c\x9c\xf2\xb5\xbe$\xf1\r\x02\xc8\xf5\x87\x9cM#\xe4\x93\x8cH9\x8e:}O\x0b\x02\xc6\xfe)\x12\x7fY\xe4\xc8\xca\xb4I\xda\x95\xcc\x01\xd0~I\xb6\x9f~\xe2\xc2\xc2C\xbf\x13g\xdb\x9c\xe0\xf1\xfa%B\x91\xeb\x93\xed\xd4u2\x8b\xa6\xd6\xb6K\\A\xe29\xc1\xe8\x10\n\xc6E\x94\xcb\x83j\x87fa\xe2\x06bD\xff\x00Ue\xb6\xb5R\x9b\x056\x86\xb9\x8d.\x1e\xa0I\xc9\xc0\x0e\x9c}\x92j\xf7\x04\x18>\xad\xc0I\xce\x0f\xb7\xba\xb6\x8dYqn\xf2d\x81#\xa0\xf9\xf4)\x15f\xd3\xc3\xd5h\xdc5\xcd,u:\xf4\xfe0\x1c\\\xda\x8cw\xc2\xf6\x83\xd2"}\xfeaf<k\xa4\n/k\xda\xdfC\xe7 |.\x83\xe9\x8fy\x91\xf2M<?t\xe6\\\xed\x06w\x00\xc7\xb3\xac@ \xb7\xdc\x03?)\x1c\xad6\xabd\xda\xacu7\xf0x\xee\xd7\x0c\x87\x0fpU\xa4\x9a"N\x9e\xcf\x91\xd8\xdc\xba\x9b\xda\xf6\x98sHp\xf7#\xa7\xc8\xf0\xbe\xabgv*1\xb5\x1b\xc3\xda\x1c=\xa7\x91\xf48_-\xd4\xadM:\x8ei\xe8\xe3\xf4 \xc2\xdcx\r\xe7\xf6s\xbb\xe1\x15\x1d\xb3\xe4@$}\xc9\xfb\xab\xc6\xf6L\x91\xa2\xf2\xa7\xa2\xaf\xcb\x84\xd6\xc4\xb4\xa8]\xda\xc9\xc2\xd6\xc8\xa1A`&\x15\xc2\xc5\xaaN\xb2t\xa9\x96;\xddU\x91C\x9aU\x1c\xe6A=\x12\x9a\x94=J\x8b[\xd7q\xd12\xa0\x01\xe7\x95\x9c\xbd\xa6\x89\xf2!\xe4\xe1^\xdb3\xb6UW\x15`\x80;\xa6\xcc\xad\x14\xf2:,$\xda5\x8aL\xca^\xbc\x83\x08]\xc4\xa6\x17\xc49\xd2\xa9u\x11\x0b\xa6=\x1c\xedl\xae\x85\x02Q\x8e\xb7DQ\xb7\x86\xcf\xb2\xa6\xab\x88S\xca\xd9UH\xf3\xe9\x00\x15\xfam\x80vJ\xae\xd8\x12\xa7\xfbA\xa7\x80\x9a{\xa1?\x91\xad;V\x81\x081Gl\x945\x0b\xd3\xcc\xa2\xff\x00i\xde \'\xb1\n\xee\x9aI%UmX\xb5\xc9\xa5\xc5\x08jUJ\x91.T\x9e\x89kcQRD\xabm\xf5\x02\xd0Z\x003\xcc\xe4}\x8a\xabf!B\x8d\x032\xb0u.\xcdSk\xa1n\xbc\xe7m/\xa7N\x98sr\xe0\x1b\xc8\xea@\x91\x95\x9an\xbdp\xdd\xad,c\xd9$@$=\x9f\xde\x9e;\x19+v\xf6,\x7f\x88-M#\xe9!\xacp\x96\x98\x07\xcb\x8e\x93\xd8C@=$es\xe4\\w\x13|o\x96\x99\x90\xd4\xae\xdfU\xc0\xbd\xa09\xa0\xb0\x96\xe08\x02`\x10z\xe4\xa1\x1c\xde\xb1\xf3\xe9\x1d\xb8L\xae\xac\xc4\x92\x08\x97z\xa2=3\xf8\xb0L\xfd\xb8\xfa\xe2\x96T\ri\xe2L\x0c\xe3\x19\xe0\x84)\r\xc4\x15\x80\x80L\x1e\xc0\xce\x01*\xfa\xb6\xce\x00\xe2$\x88\x18t\xfd~\xca\x8763\xfa\xc3\xbf\x92\xe5K\xc8\x11\xc1<\x99\xcf\xc8G\n\xac\x9a\'R\xa6\x0b\\ \xcc\xb8A\x1c\x08\xfb\xff\x00\x9a\xb3O\xa8!\xfc\x00\x1as\xc0\x1f\xe6\x975\xf2g\xf9\xc7?\xaa5\xac\xdc\xdd\xad\x04\x97\x10\xd8\x13\xf0\xee\x93\xfa\x1c\xf6LF\x8b\xc3\x0c\xa7R\xa8\xaa\xf7C\xb26\xf0\x0bv\xb9\xb0\x0fB0B\xdd\xd0\xa8\xca\x9e\x90\xe9s\x07\xab\xf8\x9c?\x88\xe0g\xbc/\x9a\xe9,{\\\xf7p\xd1!\x82"I\x81\xf4\xe3\xf3ZzO4\x9c\xd7\x03\xea\x18\xf9\x8e\xc7\xd8\x8f\xea\xb3S\xe2\xcbq\xb4(\xf1\xf6\x98w\n\xcd\x18#k\xfd\x9c8\'\xe7\xfc\x91\x1f\xfaw\xea\xa7U\xa7\xa5P~\xed\x03\xfe\xd5\xac\x14\x99Z\x9c\xc4\xb1\xe3 \xe6\x0fP}\xc1B\xe8\xbe\x1fm\xbb\xaa\x96\x1fK\xcbH\x07\x96\xc4\xf5\xfa\xae\xa5\xa7h\xc2\xadl\xd6X\xda07\xa2;\xc8d\x1f\xc9$\xa7Z\x02\x89\xbc\x8e\xa9\xdd\x86\x90\xcf\xcah9\x85[\x83%%\xaf\x7f=U?\xb5\x1e\xea\x92b\xe4\x8am\xd8\x13\x0bJ$\x99\xe8\x15\x16\xd6\xe7\x94\xd6\x86\x1b\n&\xc2\x08\xa6\x9d\x10^%\x13\x7fPm\xda\x15\x96\xd4y\'\xaa_~\xec\xac\x97\xbaF\xafHQPz\xa1Z)\x99\n\xe6\xd2\x97J\xb2\xa6\x0c.\x86\xcc(\xb8T\xc4!\xef)\xf4G[0rW\xaa\x80VI\xd34j\xd0=\xbb !n\x9b%\x17[\n\xa0\xe0\xae=\xd9\x0f\xe0\x8d;\\+\xe93j\x93\xaa\xe3\n\x0f2\x10\xdb\r\x15\xde\xdcaWcL\x9c\xa9\x9a3\xca>\xd1\x82\x10\xe5KBJ\xd961r\xa3\x80\x0b\xd5\\\x85\xa8\xe5\x92Vh\xd9&\x99J|El\x1fK zN\t\xe2\x1d\xe9 \xfb\x19\t\x9d\x07.]\xdboc\xd8xsK~R"Q5i\xa1\xc5\xd3L\xf9&\xa1f\xe6\xbbh$\xe2@\x99\x00{"\xbc\'b\xca\xd5\x1e*\x92a\xb2\x19\xf0\xee\x1c\x12H\xce1\xc7t\xe6\x95-\xce\x14\xcbZjO\x96\xd0p\xed\xd2\x1a`\xfc\xe7\x1e\xe8\xeb\x0f\r\x1a\x17\x84\x83,\xda\xe6\x83\x90\x1c\xfc\x02 \xfdO\xd1sG4T\x94%\xdb7\x969S\x92\xe8>\x87\x87m\xc8\xdb\xe54O\x0e>\xa2\x0f\xcd\xd3\x0b#\xe2\x8b\x08\xd8\xc0\x03\x00is\x9b\x00;x \x01\xf2\xc9=\x8a\xfaMJd\x0cs\xec\x86\xb9\xa2\xc0\x0b\x9d\xb5\xd5K`bC\x199\x93\xfc_\xa6T\xe7\xc9\x1cu/?\x03\xc3\x17?o\xf6|tS\x1fQ9\x99\x93\xfc\x93_\x0f\xd4-\xab8\xc8\xf2\xc18\x02\x7f\xa9\xc4\xfb\xaa\xb5KB*T\x00zC\xcf\x11\x99$\x88\x8f\xec\xa3\x19\xa6\xd5u6\xb5\x94_"C\x8e\xd3\x04\x93\xdf\xdaam\'k\xeef\x951\xb5\xdb\x98\xc7\xcbz\x92\x1d\xc8\r#\xd8\xfc\xa7\xe4\xa9}\xdf\xac\x82\xec\x03\x00\xe7\x81\xfei+tz\xce\x00\x06T\xe7\xb3\xb6\x891\x9e\x812\x1e\x1c\xba06\x0f\xef\xb0\x10~\xea\x166S\x99\xa5\xd1\xf5\x16\xb2\t>\x8782\xa0\xe8\xd7\x1f\x85\xff\x00\xc8\xfc\xbd\x96\x9e\xa9Y\r\x17\xc2\xce\r\x7f\x9e\xe3\x0e\x88c]\xc8\x83;\x8c{\xf4\xec\xb4\x17O\x8c\x0e\x8b|1\x97L\xcb,\x97h\xb1\xf5@BV\xab<**<\x95:M]J4s9X;\x89R\x05r\xaf*2\xb4"\xcd6\x06\x15\xc2\xa8C9\x84\x95i\x00\x05\xc8\xd1\xd4\x99ek\x88\x10\x94\xd5\xaf.]\xb8q*V\xd6\xddJ\xb8\xc5EY-\xb90\x8b0\xae6r\xe9S\xa7\x01\x10\xd7(l\xd61(\xae\xd8\x10\x15-n\x14\xdd%\xcau\x9a\x91\x0c\x0e\xb8\x9c!\xcd%}w!\xaa\xd5Z\xc6\xcc\xa4M\xa8\xcbz}\xd0\xb6T\xcb\x8aeQ\xb0\x14\xcd\xf8*?%\x15B\xb6\xd4!\xc1\x92\x8ci\x00)kE"7\rB\xb5\xb9D\xd4z\x87\x97%\x08l\xf7\x94\x02\xa6\xe2\xac"\xdc\x10W\x0c\x92\x07S\x84\x96\xde\xc4\xdf\xc0\x92\xdfO"\xef\xcf\x02Ci\xbe\xb4\x7fl\x00\xc2=\xb2\xe6\x9f\xbaa\xab\xea\x9e]V\xb5\xcc\xddB\xb1ii\xe4\xd1s\x80\xda\xf9\x19\x89#\xdd[c]\xe2\x8b\xdfV\x99\xa5L\xe1\xb3"\xa3\xdb\xd0\x1f\xe1\x9c\x9e\xfcd%\x9a\xdd\xcb*R\xa2\x1c6\xb5\xbf\x08#m@\xdf\xc0\xe0;r\xd8= \xfc\xfcO\xa9\xc3\xea\xfdG%\xd7_\xef\xe4\xf50O\x86*}\x8a\xb5\xadD\xf9\xdb\xcb\t,\x96\xd3\x87\xb0\xb0\xb4\xe2_\xb7\xbc\x83"zuQ\xd1\xaek\x16\\Tq\x05\xc0C\x00\xdd\x00\xed\x98\x9c\xc6H\xca_{\x04\xbc3\x02D\x06\x89-$H.=\t\xce>|e0\xd3\xae\x9e\xda&\x89d\x0fMA#/y3\x93\xd7\xd3\xb7\xec\xba\xb2c\xe4\x97\x97\xaf\xc1\x8crS\xf8C\r&\xad:\xa1\xb4\xea3mFe\xe2\x0c;={\xf1\xcf\xcd=4q\xddc\xee\\Z\xe0\xe9v\xe7\r\x80q\xe9 \x93\xd3\xe1\xf4\xcc\xe3\xeeV\x87\xc3\x95!\xa2\x89<n,\xe7\r\xdd\x80=\xa0\xfeK\xa3\x0b\xe3\xedo^\x0c2\xd4\xb7\xe4>\x95\xbc\xca\xb8P\rFS\xa7\x01\x05z\xe8]\x0bl\xc5\xe9\x02\xd7\xaa\xa9p\xdc\xaes1+\x94\xa9\x12\x16\xca\x923`\xbeVW|\xa3\xc0FZ\xdb\x19L\x19j\x07(\x96J\x05\x0b\x12\xfe\xc2H\x95\x11d\x9bV\xf6C\x89B\x9b\x1f\x04[y_`\x98T\xdb\xdc\xef\t\xa6\xb1n6\x15\x9e\xd2\x9e\x1a\xe2\x0fu\x8a\x96\xcd\x9c\x07tm\xc1R\xaa\xd00\xa1WQc\x07+\xce\xac\xd70\xbb\xea\x8eC\xe3\xad\x14y\xc0\x14E;\xb1\xc2\xce\x1b\x99s\xa1r\x8d\xd4;)\xad\xf6M\xd7F\xae\x93\x82\x8d\xcb\xb1)m\xbd\xfbq\x95\xcb\xfd@B+bl\x1a\xe2\xac\x95_iT\xd1\xac\x17.+ao\xc9$a\xc6\xd9\xa3\xb1`\r\x95]\xcd\\\xa5V\x1a\x9f\xa6%\rWU\x87B\xc5=\xdb5\xaf\x08t\xd6\x9eT\xa9\xc9(zz\x9bv\xa2\xb4\xfa\xc1\xd9O\x95\x8f\x8d\x1d\xb8\x10\xa5M\xa6\x17k\xd7n\xe8U\xdc\xdd\x00\xa6\xf4"u\xeb\x06\x8c\xa1\xdfz\xcaFj\x10\x1c`\xb5\xae\xc0d\xf5q\xe8y>\xc0\x18\x04\x82\xa8\xb9\xdd\xc4\x80\xe2\x083\x00S\x18\x97<\x9f\x84\t\xf9\x9e>y\xedp\xfa\xfc\xb6\xc8\x19\x0f$\xcf\x95LA%\xe7\x9d\xd0\x04\xf6\x91\xd6W\x16\\\x9c\x9d.\x8e\xbcx\xf8\xab}\x8c\xb5Mh9\xde\xa6\xee\xa7\xb8?`0*\x9cC\xdcO\r\x98\xda3<\xe4\x91\x19\xeb\xe0\xfa\x8fq{2\xe7\x06\x86\t\x0e\x03\xa4FO\\\x98\x8e\xc3\x10e\xb5\x1d\x80\xb8\xc3@\x8d\xafp\x9f/\x10\x08\x02a\xc4\x03\xea2UwZ\x847\xf7p\x04\x07\xb9\xee\x91U\xfb\x8e`N&z\xe7\x12}\xb2R\xdd!\xbd\x02[Q\x10\xf3\x10\x06[\xb5\xb8\x99\xfc\xce\x04\x98\xeb\xd1p\xea;[\x90\x08\x13\x983\x809?(\xfb}\xe4]\xbe\t.\r\'.=b0\xde\xe0g<*\xaa\xb9\xae\x0ef\x08\x0e\x0fh\xcf \xb9\xbf\xcd\xbfe]3\x190\xbd&\xb8\xa8\xf79\xe0\xb5\xb1!\xce\xf8\xa2G\xa5\x82d\x93\xf4\xef\xd1<\xd1*\x80\xfe\xb1\x12\xd9 \xc0t\x11\xf7\x10RM&\x9b\x9c\xe20v\x81=\x0bd\x9c\x7f?t\xd1\x94\x83\x1c\xd6\xb7\x1c{\xad\xf1\xad\x08\xd8\x03*\xbb\xabM\xc83y\xb5\xa1\x19J\xe0\x96\xca\xddZ\xd8\xb5\xd3!N\xd4D+\xa9[\x80\x96[^\x13P\x84\xe9\x81O&\x14\x8a\xa8\xd0\x89+\xce2a\x0b\xa8\xde\xec\x05\r\xa6]\xee2\xa5\xdd\x8fC\x03D)\n!Wq^\x14)\xdc\x08\x08\xe4:\x13]\xeb\xc1\xc2\x12W\xd42\\\x12\xc2\xc3(\xa0\xfcB\xb6\x83\xb0{\xcb\xe2]\x12\x98R\xd5Hf\xd9\xe8\x92\xd6g\xa9L\xb1[3\xd8\xc2\xc6\xbeI=T\xeb\xbeJ\n\x81\x85\xda\xceR\xcaE\x8f\xba-8+\xaf\xb9.@T\x08\x9a|&$\x19N\xea\x14\xeb]\x02\xd4\xb1\xe1Z\xc1\x84\x05"\xeaU`!+U\xcc\xa9\xb9\xca\x87\x04P\x82\xa9\xde`\x05\xa1\xd3\xef\x80g+"\x1a\xae\xa5\\\xf0\x98\x87\xb4\xef\xe6\xa4\x92\x9eZ\xb4\xd4 \xb7\x04\r\xc0\x93\x11\x1f\x8b\x83\x00w\xfbJ\xcf\xe9ZvC\xea\x90\x06N\xc2`\x909\'\x07\x1e\xc0\x19\xe3\x9c\x17\x15\xb5X\xa6\\\xd3\xb5\xa6E\x16\xe0:\xb3\x84C\xcee\xac\xfe\x11\x9e\x0b\x8c\x98\'\x93.U\xfaS:1\xe3\xfd\xcc\xee\xa3x)\x91M\xbb7\x0fS\xe0\xcbim\x9f\x88\xe4\xe2I\xef\'\xd9)\xd3m\xdbX\xb9\xc5\xc2\x9d\x00\xe9}I%\xd5H"\x06\xe8\xf5\x1e\x047\xa8\xf6\x0b\xb4t\xca\xbb7T\x88.k\xea\x8c\xeey\x80Z\xc0\x06H\x02Lu\xc8\xe3\x04\x8b\xdar\xd2E1 me0\xd0\x1c3\xc6\x0e\xd1\x88\xf4\x83\x8e\xd9X\xacrh\xd2SI\x82\xeb\x15i\xb9\xd1M\xc4\xd3h\x0ckX\xd7H\x18\xe4\xf0\x04\xf5\xc98JZ\xf6\xb4\x82=@FL\x97\x12\'\x04\x9e\x13\x068\x16\x86\x97:\x1e\xed\xcd\xa6\\\xd6\xb5\x8fh\x87d\x1c\xb7\xdb\x9eP\xef\xaa\xeaD\x02\xe6\xbb\x04b^& \x00[#t`I$c\x84\xbd\x1f\xc1\x93\x95\xf6G\xcc\x0f"?\t.{\xbe\x16\xcf\xa6C1\x91\xd3\xa4D\x84=\xf5\xb9%\xc4\x10\xde zw\x98w1\xd0`\xfd\xd1u\x0b\x1b\xb1\xc0\x13\xb8\x12\t\r\xc1\';\xbb\x19\x91\xca\x85w\xedq|\xcb\xc8\x03\xa1\x0ch\xe9\xf3\xf7]J\x17\xa36\xc2\xed\xdb\xe5\xc3D\x020\xe2\'\xd4{\x9fu\xef>\x1c\t\xee\x95\xd3\xaeAWU|\xad\xb8P)\r\xee\xb5\t\x88G\xda\xea\xe02:\xac\xc3]\x0b\x8e\xac\x86\x85cZz\x8cU\xdd\xd2V\xc3N\xd4\x9a\xe6\x8c\xaf\x9d4\xab\xed\xef\x0bp\n\x1cm\r3K\xe2\x1b\xf6\x9e9\xe1(\xd3\xf5=\xa5(\xaftI\xc9Q=\xd0\xa3\xf2\'#Au\xabO\x08Q\xab\x94\xa4UP\xde\x8e!\xc8.\x89\xc2\xaa\xadEu\x1f\x85\tS\x94\x8a\xbd\x10 \x95e0Ti\xa9\x94\xecE\xb2\x15\x15*eI\xe8r\x81\xd9\xca\x8eW\xb5\xc6\x15\x0eW\xd2\xe12QQ%[A\xea\xba\x8b\xd4\xd0#\xb5\xaaB\xe5#*\xab\x85\xdbNSB\xf2\x10i\x9e\x00\x92p\x00\xc9$\xf0\x00G\xda[\xb1\x90^\xe0\x1cf\x0fA\x1f\x16\xd8\xe4\x0e\xae\xfa\x0e\xe7\xda\x7f\xfb\xc1\xff\x00\x05O\xff\x00\'\xa1\xef\xba\x7f\xcb\xbf\xfct\x97>y\xb5\xed^M\xf1A~\xa1\x85J\xdb\xc0\xaa\xe2|\xa6\x8f\xdd\xfa\x83Ms\x99!\xa3\xf0\x00N\x01\xc9\x81\xd5YiE\xb5\x1d\xbe\xb3\xbdr\xd2\x1a\xf9\x9aL?\x0b\xa0\x1c\xbc\x86\xb6\x00\xeag\xf0\xaa\xbcM\xfe\xe5\xdf\xf2\xe3\xfclV\xbf\x93\xff\x000\xdf\xd0.H\xab\x9a5\x93\xd34\x0c\xb6\x04@\x07hk\x9c\xec\x90r!\xbfX\xe7\xe4;\xa5\xd5[\xf8F\xe7\t\x87g/\x7fP\x0fF\x80}\xff\x00\x0fR\x9f\xd4\xe3\xfb\xdf\xe1\xa2\x94\\|l\xfa\xff\x00\x89\xeb\xb5\x1c\xc6n\xadb\xda\xb3\xb8\x81>\x9f\xc0\xc7\x00a\xcci\xf8Ld\xe7\xb1\x80\x84k\x18\xfa\xa4\x97l\xa7\x8c\tnOb\xdc\xfe\x10q\x1c\'\xad\xff\x00\xdbS\xff\x00\xebg\xe8R\x1a?\x18\xff\x00\x8f\xfe\xd4P\x05\\\xdc1\xbe\x86{L\xf4>\xfe\xff\x00\xa7\xcd\x0c\xe7a\x07K\x94I[qH\xce\xec\x81r\xf0%p"m\xd3\xb1\xa4U\xe6\x1e\xcb\x90U\xef\xe5u\xa9XQ\x16L!w\x99L\xba \x9d\xcai\x83\x06{\xb2\xa5\xbc\xaeU\xe5\\\xc4\xc9E@\xa9\xe7\xb2\xb0\xabRl\xa4\x8f\xff\xd9'  # noqa: E501
BINARY = bytes(BINARY)