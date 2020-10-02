import os
import sys
import warnings
from typing import List
from itertools import chain
from PIV import __version__
from numpy import __version__ as numpy_version
from matplotlib import __version__ as matplotlib_version
from PIL import __version__ as pillow_version
# -------------------------------------
assert sys.version_info >= (3, 6, 0), "PIV requires Python 3.6+"

if numpy_version != "1.19.2":
    msg = f"""
    Numpy version is below version 1.19.2. 
    Linspace may or may not exist in your numpy version of {numpy_version}.
    Consider upgrading numpy.
    """
    warnings.warn(msg, DeprecationWarning)
    
if matplotlib_version != "3.3.2":
    msg = f"""
    Matplotlib version is below version 3.3.2. 
    Some functions may or may not exist in your matplotlib version of {matplotlib_version}.
    Consider upgrading matplotlib.
    """
    warnings.warn(msg, DeprecationWarning)
    
if pillow_version != "7.2.0":
    msg = f"""
    Pillow version is below version 7.9.2. 
    Image may or may not be the same as the 7.2.0 Image class. 
    Your current Pillow version: {pillow_version}.
    Consider upgrading Pillow.
    """
    warnings.warn(msg, DeprecationWarning)
    
# -------------------------------------
from pathlib import Path
CURRENT_PATH = Path(__file__).parent
sys.path.insert(0, str(CURRENT_PATH))

try:
    import rstparse
    
    parser = rstparse.Parser()
    with_rst_parse = True
except ImportError:
    import codecs
    with_rst_parse = False

def get_requirements(filename) -> List[str]:
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


if "setuptools" in sys.modules:
    from setuptools import setup, find_packages
    module_requirements = get_requirements(CURRENT_PATH / "requirements.txt")

    extra_reqs = {
        'test': get_requirements(os.path.join(os.path.abspath('./docs'), 'dev-requirements.txt')),
        'doc': get_requirements(os.path.join(os.path.abspath('./docs'), 'docs-requirements.txt'))
    }

    extra_reqs['all'] = list(chain(extra_reqs.values()))
    
    with_setuptools = True
else:
    from distutils.core import setup
    
    reqs = {
        'main': get_requirements(CURRENT_PATH / "requirements.txt"),
        'test': get_requirements(os.path.join(os.path.abspath('./docs'), 'dev-requirements.txt')),
        'doc': get_requirements(os.path.join(os.path.abspath('./docs'), 'docs-requirements.txt'))
    }
    
    reqs['requirements'] = list(chain(reqs.values()))
    
    with_setuptools = False

def get_l_desc() -> str:
    long_desc = ""
    change_log = ""
    if with_rst_parse:
        doc = []
        with open(CURRENT_PATH / "README.rst", encoding='utf-8') as r:
            parser.read(r)
            
        parser.parse()
        for line in parser.lines:
            doc.append(line)
        
        for item in doc:
            long_desc += item + '\n'
            
        del doc
        cl_doc = []
        with open(CURRENT_PATH / 'docs' / 'CHANGELOG.rst', encoding='utf-8') as c:
            parser.read(c)
            
        parser.parse()
        for line in parser.lines:
            cl_doc.append(line)
        
        for item in cl_doc:
            change_log += item + '\n'
            
        long_desc = (long_desc +  # noqa: W504
                     '\n' +  # noqa: W504
                     change_log)
    else:
        long_desc = (codecs.open(
            CURRENT_PATH / 'README.rst', 'r', 
            'utf-8',).read() +  # noqa: W504
            '\n\n' +  # noqa: W504
            codecs.open(
                CURRENT_PATH / 'docs' / 'CHANGELOG.rst', 'r',
                'utf-8').read())
        
    return long_desc

def get_license() -> str:
    return(
        (CURRENT_PATH / "LICENSE").read_text(encoding='utf-8')
    )


SHORT_DESC = """
PIV provides tools to converting, enhancing pictures and videos in python.
"""

# -------------------------------------
if with_setuptools:
    setup(
        name="Python Image and Video Tools",
        version=__version__,
        description=SHORT_DESC,
        long_description=get_l_desc(),
        long_description_content_type='text/x-rst',
        author="Sergio Ley",
        author_email="ghub4127@gmail.com",
        url="https://github.com/SLey3/Python-Image-and-Video-Tools",
        download_url="",
        packages=find_packages(),
        license=get_license(),
        keywords=[
            'Image',
            'Video',
            'manipulation',
            'processing',
            'convertion'
        ],
        platforms='win32',
        install_requires=module_requirements,
        extras_require=extra_reqs['all'],
        tests_require=extra_reqs['test'],
        python_requires=">=3.6",
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Win32 (MS Windows)',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: Microsoft :: Windows :: Windows 10',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.8',
            'Topic :: Multimedia :: Video :: Conversion',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Utilities'
        ]
    )
else:
    setup(
        name="Python Image and Video Tools",
        version=__version__,
        description=SHORT_DESC,
        long_description=get_l_desc(),
        author="Sergio Ley",
        author_email="ghub4127@gmail.com",
        url="https://github.com/SLey3/Python-Image-and-Video-Tools",
        download_url= "",
        packages=["PIV"],
        license=get_license(),
        install_requires=reqs['requirements'],
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Win32 (MS Windows)',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: Microsoft :: Windows :: Windows 10',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.8',
            'Topic :: Multimedia :: Video :: Conversion',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Utilities'
        ]
    )