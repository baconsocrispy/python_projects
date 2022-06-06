# code from error-handling lesson
def get_info():
  var1 = input('Please provide the first numeric value: ')
  var2 = input('Please provide the second numeric value: ')
  return var1, var2

def compute():
  go = True
  while go:
    var1, var2 = get_info()
    try:
      var3 = int(var1) + int(var2)
      go = False
    except ValueError as e:
      print('{}: Must provide numeric value'.format(e))
    except:
      print('Invalid entry')
  print("{} + {} = {}".format(var1, var2, var3))

# Execute your own try/except/finally block
cocteau_twins = ['Elizabeth Fraser', 'Robin Guthrie', 'Will Heggie', 'Simon Raymonde']

def get_twin():
  print('Cocteau Twins: ' + ', '.join(cocteau_twins))
  twin = input('Who is your favorite Cocteau Twin???\n>>>')
  return twin

def twinnage():
  go = True
  while go:
    twin = get_twin()
    try:
      cocteau_twins.index(twin)
      go = False
    except:
      print("THAT IS NOT A COCTEAU TWIN!")
  print('Correct, {} is the best Cocteau Twin.'.format(twin))


if __name__ == "__main__":
   twinnage()
