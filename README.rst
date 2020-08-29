============================
Python Image and Video Tools
============================
Python Image and Video Tools provides support for Image and Video editing. 

**Using the `ImageTools` class to convert an image file:**

.. code-block:: python

    from PIV import ImageTools
    import os

    path = os.path.expanduser(os.getenv('USERPROFILE')) + '\\name.png'

    image = ImageTools(path, False)

    image.convertFile(".jpg")

Along with being able to convert files...