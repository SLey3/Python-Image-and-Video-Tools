import os

def name(path: str) -> str:
    """
    finds name for file
    """
    name_extension = os.path.basename(path)
    return name_extension.rsplit(".", 1)[0]

def extension(path: str) -> str:
    """
    finds extension
    """
    base_name = os.path.basename(path)
    name = os.path.splitext(base_name)
    extension = name[1]
    return extension