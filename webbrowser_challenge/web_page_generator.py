# create a Python script that will automatically generate an html file
# the script should open the file in a new tab
# a tkinter GUI should allow users to enter and update the html body text

#import modules 
import webbrowser
import os

# writes to file - 'w' indicates write 
# creates new file if it doesn't exist
def write_to_file(file_path, text):
  with open(file_path, 'w') as file:
    file.write(text)

# opens html file in default web browser
def open_in_browser(file_path):
  absolute_path = os.path.abspath(file_path)
  webbrowser.open_new_tab('file:///' + absolute_path)

# calls above functions in one 
def write_and_open(file_path, text):
  html = update_text(text)
  write_to_file(file_path, html)
  open_in_browser(file_path)

# plugs user text into html body
def update_text(text):
  html = '<html>\n<body>\n<h1>\n{}\n</h1>\n</body>\n</html>'.format(text)
  return html


if __name__ == "__main__":
 pass
