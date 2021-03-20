import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

if path.exists("textfile.txt"):
  # get the path to the file in the current directory
  src = path.realpath("textfile.txt")

  # make a backup copy by adding ".bak" to the end
  dst = src + ".bak"

  # copy over permissions, modification times, and other info
  # shutil.copy(src, dst)
  # shutil.copystat(src, dst)

  # rename the original file
  # os.rename("textfile.txt", "newfile.txt")

  # putting things into a ZIP archive
  # root_dir, tail = path.split(src)
  # shutil.make_archive("archive", "zip", root_dir)
  
  # more fine-grained control over ZIP files
  with ZipFile("testzip.zip", "w") as new_zip:
    new_zip.write("textfile.txt")
    new_zip.write("textfile.txt.bak")