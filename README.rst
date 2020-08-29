============================
Python Image and Video Tools
============================
Python Image and Video Tools is a Image and Video tool provider that helps developers with editing an Image or a Video 
and get information on the Image or Video file.

News
~~~~~~~~~~~~~~~~~~

Examples
~~~~~~~~~~~~~~~~~~
Using the ``ImageTools`` class to convert an image file:

.. code-block:: python

    from PIV import ImageTools
    import os

    path = os.path.expanduser(os.getenv('USERPROFILE')) + '\\name.png'

    image = ImageTools(path, False)

    image.convertFile(".jpg")

Installation
~~~~~~~~~~~~~~~~~~

Contribution
~~~~~~~~~~~~~~~~~~

.. figure:: docs/CONTRIBUTING.md