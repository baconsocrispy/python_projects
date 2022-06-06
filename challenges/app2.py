# dunder methods
import app

def print_app2():
  name = (__name__)
  return name

# tests whether code is being called from another file or run directly
if __name__ == "__main__":
  # calling code from within the file
  print("I am running code from {}".format(print_app2()))
  # calling code from an external file
  print("I am running code from {}".format(app.print_app()))