PIV - ImageTools
****************

**Description**
----------------

The ``ImageTools`` class is provided as a way to get information like binary data, image name, image path, image size,
and added with functions like converting an Image file.

**Initialization**
------------------
In order to use the ``ImageTools`` class, you must first initialize the class. This is to make sure that the image file does exists
and isn't and video file or it doesn't exist. If the file was a video file, then ``ValueError`` would be raised and if the file
doesn't exist, then a ``ImageNotFound`` error would be raised.

**Arguments:**

- `image`: The image name with the file extension or the path to the image would be placed here. **This must be a string**.
- `perm_save` (`experimental`): If true, then the path would be saved in the `PERM_SAVE` list, where the path can be accesed for future use. **This must be a boolean**.

**Initialization Usage:**

**Method#1:**

.. code-block:: python

    image = ImageTools('path/to/image', True)

**Method#2:**

.. code-block:: python

    with ImageTools('path/to/image', False) as i:
        # Code here

**ImageTools Class Functions**
------------------------------
_format
~~~~~~~
format of the image