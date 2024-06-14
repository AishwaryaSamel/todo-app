import zipfile
import pathlib

""" zipfile.ZipFile is a type object, 
    zipfile is a standard library name and 
    ZipFile is a type
"""


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "../zipfiles/compressed.zip")
    with zipfile.ZipFile(dest_path,'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

if __name__ == "__main__":
    make_archive(["e1.py","e2.py","e3.py","e4.py"], "../dest")
