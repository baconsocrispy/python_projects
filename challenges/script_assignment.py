# Requirements

# 1. script must use python 3 + OS Module
# 2. must use list() method to iterate through all files in directory
# 3. must use path.join() to concatenate absolute path elements
# 4. must use getmtime() to find latest create/modify date
# 5. must print each txt file & mtime to console

# Python Version: 3.10.4

# importing OS Module
import os

# creating path to txt file directory
txt_path = 'txts/'
abs_path = os.path.abspath(txt_path)

# use listdir() to collect files into a list
all_files = os.listdir(abs_path)

# iterates through files and joins .txt file path to absolute path
# obtains the mtime and saves it to a variable
def find_txts():
  for file in all_files:
    path = os.path.join(abs_path, file)
    mtime = os.path.getmtime(path)
    if '.txt' in file:
      print_file(path, mtime)

# opens and reads files to variable
# prints file contents and mtimes to console
def print_file(path, mtime):
  file = os.open(path, os.O_RDONLY)
  text = os.read(file, 1000)
  print(text)
  print(mtime)
  os.close(file)

# calls main function
if __name__ == "__main__":
  find_txts()