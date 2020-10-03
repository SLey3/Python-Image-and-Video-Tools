# flake8: noqa

import os
import sys
import shutil
# import pytest
from PIV import ImageTools
from PIV.base import BINARY, FILE_EXTENSIONS

# Image path
TEST_VIDEO_DIR = os.path.normpath(os.path.abspath('.') + '/docs/test_utils/test_video/pop.mp4')
TEST_IMAGE_DIR = os.path.normpath(os.path.abspath('.') + '/docs/test_utils/test_images/testbird.jfif')

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
    assert ext() == '.jfif'

def name():
    # first initializes the Imagetools class
    test_image = ImageTools(TEST_IMAGE_DIR, False)
    # finally, calls the name property
    test_name = test_image._name
    return test_name

def test_name():
    assert name() == 'testbird'
 
#@pytest.fixture
def size():
    # first initializes the Image tools class
    test_image = ImageTools(TEST_IMAGE_DIR, False)
    # finally, calls the size property
    test_size = test_image.size
    return test_size


def test_size(size):
    assert size == (251, 201)

def path():
    # first initializes the Image tools class
    test_image = ImageTools(TEST_IMAGE_DIR, False)
    # finally, calls the path property
    test_path = test_image.path()
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
    test_image.convertFile(".png", '..\\result_images', True)  # in this test, we're converting a .jfif image file into a .png image file
    
def test_convertion():
    convertion()
    os.chdir(os.path.normpath(os.path.join(os.getcwd(), 'docs', 'test_utils', 'result_images')))
    assert os.path.isfile('testbird.png') == True
    
def rep():
    # first initializes the Imagetools class
    test_image = ImageTools(TEST_IMAGE_DIR, False)
    # finally, calls the __repr__ dunder function
    return repr(test_image)

def test_rep():
    test = ImageTools(TEST_IMAGE_DIR, False)
    assert rep() == repr(test)
    
def file_exts():
    # Skips initialization as image is not needed and calls the available_exts property
    extensions = ImageTools.available_ext()
    return extensions

def test_exts():
    assert file_exts() == sorted(FILE_EXTENSIONS['image'])
    
def test_graph():
    # Calls the graph function from the ImageTools class
    ImageTools.graph(
        [0,10], [0,10], [
            [
                (0,0), (2,2), (4,4), (6,6), (8,8), (10,10)
                ], [
                    (0,5), (2,5), (3,5), (4,7), (5,7), (6,8), (7,8), (8,10), (10,10)
                    ],
                [
                    (3,3), (6,6), (9,9), (9,6), (10,3)
                ]
            ],
        title="Test Example without Numpy Linspace", y_title= "Y Axis", x_title="X Axis", 
        labels=["line#1", "line#2", "line#3"], image_name="Graph#1", include_legend=True)
    DEST_PATH = os.path.abspath('./docs/test_utils/result_images')
    SRC_PATH = os.path.join(os.path.abspath('.'), "Graph#1.jpeg")
    shutil.move(SRC_PATH, DEST_PATH)
    TEST_PATH = os.path.join(DEST_PATH, "Graph#1.jpeg")
    assert os.path.isfile(TEST_PATH) == True
    
# def test_lingraph():
#     # Calls the graph function from the ImageTools class
#     ImageTools.graph(with_linspace=True, lin_start=5, lin_end=50, lin_num=100,
#                      lin_quadratic=True, lin_cubic=True, 
#                      labels=["Lin linear", "Lin Quadratic", "Lin Cubic"], include_legend=True, 
#                      title="Graph with Numpy Linspace", y_title="Y axis", x_title="X axis", image_extension=".png",
#                      image_name="Linspace_Graph")
    
#     DEST_PATH = os.path.abspath('./docs/test_utils/result_images')
#     SRC_PATH = os.path.join(os.path.abspath('.'), "Linspace_Graph.png")
#     shutil.move(SRC_PATH, DEST_PATH)
#     TEST_PATH = os.path.join(DEST_PATH, "Linspace_Graph.png")
#     assert os.path.isfile(TEST_PATH) == True