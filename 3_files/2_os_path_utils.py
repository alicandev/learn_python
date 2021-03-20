import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

print("the name of the OS")
print(os.name)
print("\n")

print("check for item existence and type")
print("item exists: " + str(path.exists("textfile.txt")))
print("item is a file: " + str(path.isfile("textfile.txt")))
print("item is a directory: " + str(path.isdir("textfile.txt")))
print("\n")

print("work with file paths")
rp = path.realpath("textfile.txt")
print("item path: " + str(rp))
print("item path and name " + str(path.split(rp)))
print("\n")

print("get the modification time")
mt = path.getmtime("textfile.txt")
print(time.ctime(mt))
dtmt = datetime.datetime.fromtimestamp(mt)
print(dtmt)
print("\n")

print("calculate how long ago the item was modified")
td = datetime.datetime.now() - dtmt
print(f"it has been {str(td)} since the file was modified")
print(f"or, {str(td.total_seconds())} seconds")