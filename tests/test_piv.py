import os
import sys
import shutil
try:
    from PIV import ImageTools
    from PIV.base import BINARY
except ImportError:
    sys.path.append(os.path.abspath('../PIV'))
    from PIV import ImageTools
    from PIV.base import BINARY
# Image path
PARENT_DIR = os.getcwd()
__dir__ = PARENT_DIR + '\\Images\\testbird.jfif'
TEST_IMAGE_DIR = os.path.normpath(__dir__)

# tests

def height():
    # first initializes the Imagetools class
    test_image = ImageTools(TEST_IMAGE_DIR, False)
    # finally, calls the height property
    test_height = test_image._height
    return test_height

def test_height():
    assert height() == 251
    
def width():
    # first initializes the Imagetools class
    test_image = ImageTools(TEST_IMAGE_DIR, False)
    # finally, calls the width property
    test_width = test_image._width
    return test_width

def test_width():
    assert width() == 201

def ext():
    # first initializes the Imagetools class
    test_image = ImageTools(TEST_IMAGE_DIR, False)
    # finally, calls the format property
    test_format = test_image._format
    return test_format

def test_ext():
    assert ext() == 'jpeg'

def name():
    # first initializes the Imagetools class
    test_image = ImageTools(TEST_IMAGE_DIR, False)
    # finally, calls the name property
    test_name = test_image._name
    return test_name

def test_name():
    assert name() == 'testbird'
    
def size():
    # first initializes the Image tools class
    test_image = ImageTools(TEST_IMAGE_DIR, False)
    # finally, calls the size property
    test_size = test_image.size
    return test_size

def test_size():
    assert size() == (251, 201)

def path():
    # first initializes the Image tools class
    test_image = ImageTools(TEST_IMAGE_DIR, False)
    # finally, calls the path property
    test_path = test_image._path
    return test_path

def test_path():
    assert path() == TEST_IMAGE_DIR

def binary():
    # first initializes the Image tools class
    test_image = ImageTools(TEST_IMAGE_DIR, False)
    # finally, calls the binary property
    test_bin = test_image._binary
    return test_bin

def test_binary():
    assert binary() == BINARY
    
def convertion():
    # first initializes the Imagetools class
    test_image = ImageTools(TEST_IMAGE_DIR, False)
    # Then calls the file extension converter
    test_image.convertFile(".png") # in this test, we're converting a .jfif image file into a .png image file
    # after image is created, we're going to move the created .png image to the tests/image directory
    # shutil.move(os.path.join(os.getcwd(), 'testbird.png'), os.path.normpath(os.getcwd() + '\\tests\\Images'))
    
def test_convertion():
    assert convertion()
    
def rep():
    # first initializes the Imagetools class
    test_image = ImageTools(TEST_IMAGE_DIR, False)
    # finally, calls the __repr__ dunder function
    return repr(test_image)

def test_rep():
    assert rep() == "ImageTools('C:\\Users\\ghub4\\OneDrive\\Desktop\\Python-Image-and-Video-tools\\tests\\Images\\testbird.jfif', False)"
    
