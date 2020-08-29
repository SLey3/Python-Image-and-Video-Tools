.. TODO
.. 1) Fill in outline
.. 2) add all possible small tags to the README doc
.. 3) Improve the README doc for any errors and add more explanation

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
    :linenos:

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