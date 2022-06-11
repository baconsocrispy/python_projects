# 1. create 2 folders labeled a and b
# 2. create four .txt files
# 3. create a script that will transfer files from a to b

import shutil
import os
import time

# transfers modified files from one folder to another
def transfer_modified_files(folder_a, folder_b):
  modified = get_modified(folder_a)
  for file in modified:
    shutil.move(folder_a + '/' + file, folder_b)
# returns a list of files that have been modified in the last 24 hours
def get_modified(folder):
  modified = []
  files = os.listdir(folder)
  for file in files:
    file_path = folder + '/' + file
    if is_modified(file_path):
      modified += [file]
  return modified
# checks if the files have been modified in the last 24 hours (86,400 seconds)
def is_modified(file):
  mod_time = os.path.getmtime(file)
  return (time.time() - mod_time) < 86400

if __name__ == "__main__":
  pass
