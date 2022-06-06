# Python Version: 3.10.4
# 
# Purpose: Putting Python principles together in one project
#          as part of the Tech Academy Python Course.


def start(nice = 0, mean = 0, name = ""):
  name = describe_game(name)
  nice, mean, name = nice_mean(nice, mean, name)

def describe_game(name):
  if name != "":
    print("\nThank you for playing again, {}.".format(name))
  else:
    stop = True
    while stop:
      if name == "":
        name = input("\nWhat's yer name???\n>>>").capitalize()
        if name != "":
          print("\nWelcome, {}".format(name))
          print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
          print("but at the end of the game your fate will be sealed by your actions.")
          stop = False
  return name

def nice_mean(nice, mean, name):
  stop = True
  while stop:
    show_score(nice, mean, name)
    pick = input("\nA stranger approaches for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>>").lower()
    if pick == "n":
      print("\nThe stranger walks away smiling...")
      nice = (nice + 1)
      stop = False
    if pick == "m":
      print("\nThe stranger glares at you \nmenacingly and storms off...")
      mean = (mean + 1)
      stop = False
    else:
      print("\nAnswer must be N or M")
  score(nice, mean, name)

def show_score(nice, mean, name):
  print("\n{}, your current totals: \n({} Nice and {} Mean)".format(name, nice, mean))

def score(nice, mean, name):
  if nice > 2:
    win(nice, mean, name)
  if mean > 2: 
    lose(nice, mean, name)
  else:
    nice_mean(nice, mean, name)

def win(nice, mean, name):
  print("\033[1;32;40m \nNice job {}, you win. \nEveryone loves you and you've \nmade lots of friends along the way.".format(name))
  again(nice, mean, name)

def lose(nice, mean, name):
  print("\033[1;31;40m \nAhhh too bad, game over. \n{}, you live in a dirty beat up \nvan by the river, wretched and alone.".format(name))
  again(nice, mean, name)

def again(nice, mean, name):
  stop = True
  while stop:
    choice = input("\nDo you want to play again? (y/n)\n>>>").lower()
    if choice == "y":
      stop = False
      reset(nice, mean, name)
    if choice == 'n':
      print("\nAh, so sad, sorry to see you go.")
      stop = False
      quit()
    else:
      print("\nEnter (Y) for 'Yes' or (N) for 'No'\n>>>")
def reset(nice, mean, name):
  reset_text = print("\033[1;37;40m")
  nice = 0
  mean = 0
  start(nice, mean, name)

if __name__ == "__main__":
  start()



