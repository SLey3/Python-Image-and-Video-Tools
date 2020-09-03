PIV - ImageTools
****************

**Description**
----------------

The ``ImageTools`` class is provided as a way to get information like binary data, image name, image path, image size,
and added with functions like converting an Image file.

**Initialization**
------------------
*In order to use the ``ImageTools`` class, you must first initialize the class. This is to make sure that the image file does exists
and isn't and video file or it doesn't exist. If the file was a video file, then ``ValueError`` would be raised and if the file
doesn't exist, then a ``ImageNotFound`` error would be raised.*

**Arguments:**

- `image`: The image name with the file extension or the path to the image would be placed here. **This must be a string**.
- `perm_save` (`experimental`): If true, then the path would be saved in the `PERM_SAVE` list, where the path can be accesed for future use. **This must be a boolean**.

**Initialization Usage:**

**Method#1:**

.. code-block:: python
    :linenos:

    image = ImageTools('path/to/image', True)

**Method#2:**

.. code-block:: python
    :linenos:

    with ImageTools('path/to/image', False) as i:
        # Code here

**ImageTools Class Functions**
------------------------------
_format
~~~~~~~
*Returns the Image extension.*

_name
~~~~~
*Returns the name of the Image.*

_width
~~~~~~
*Returns the width of the Image.*

_height
~~~~~~~
*Returns the height of the Image.*

_binary
~~~~~~~
*Returns the binary data of the Image.*

size
~~~~
*Returns the size of the Image (Both width and height).*

available_ext
~~~~~~~~~~~~~
*Returns all of the image extensions that are currently supported.*

.. note::
    *This function can be used without initializing the class.*

.. todo::
    *Fix the function from printing the list two times.*

path
~~~~
*Returns the filepath of the Image file.*

**Argument:**
- `save`: If True then it will save the filepath to the pathlist chosen when the class was initialized.
Otherwise, the `save` argument will return False.

**Example:**

.. code-block:: python
    :linenos:

    # Example file structure:
    # ImageTesting
    # |  Image_path_example
    # |                    | path_test.py
    # |  cat.png
    #
    # Example:

    with ImageTools('cat.png', True) as i:
        path = i.path(True)
    print(path)
    # prints: c:\Users\mack\ImageTesting\cat.png

.. todo::
    *Make showing example in an online IDE like repl*