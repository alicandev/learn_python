# open a file for writing and create one if it doesn't exist
# f = open("textfile.txt", "w+")

# open a file for appending text to the end
# f = open("textfile.txt", "a")

# open a file for reading
f = open("textfile.txt", "r")

# write some lines of data to the file
# for i in range(10):
#   f.write(f"This is line {str(i)}\r\n")

# read the contents of a file
# if f.mode == "r": # check if the file was successfully opened
#   contents = f.read()
#   print(contents)

# read the contents of a file line by line
if f.mode == "r":
  ls = f.readlines()
  for l in ls: print(l)

# close the file when done
# f.close()
