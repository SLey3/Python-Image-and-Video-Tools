.. TODO
.. 1) Fill in outline
.. 2) add all possible small tags to the README doc
.. 3) Improve the README doc for any errors and add more explanation

============================
Python Image and Video Tools
============================
.. image:: https://travis-ci.com/SLey3/Python-Image-and-Video-Tools.svg?token=BwisYM6yx8jxt6nje3y4&branch=master
    :target: https://travis-ci.com/SLey3/Python-Image-and-Video-Tools

.. image:: https://app.fossa.com/api/projects/git%2Bgithub.com%2FSLey3%2FPython-Image-and-Video-Tools.svg?type=shield
    :target: https://app.fossa.com/projects/git%2Bgithub.com%2FSLey3%2FPython-Image-and-Video-Tools/refs/branch/master/252f4ffda6b16091c8d82dd6c0df5450b6d05f09
    
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

Using the ``ImageTools`` class to convert an image file using a **with statement**:

.. code-block:: python

    from PIV import ImageTools
    import os

    path = os.path.expanduser(os.getenv('USERPROFILE')) + '\\name.png'

    with ImageTools(path, False) as i:
        i.convertFile(".jpg")


Installation
~~~~~~~~~~~~~~~~~~

Contribution
~~~~~~~~~~~~~~~~~~
.. figure:: docs/CONTRIBUTING.md
