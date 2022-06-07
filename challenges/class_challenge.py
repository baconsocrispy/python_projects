# 1. create a class
# 2. create an object
# 3. assign values to object properties using __init__() function
# 4. create a method in a class

# creating a class
class TalkingHead:
  def __init__(self, first_name, last_name, instruments):
    self.first_name = first_name
    self.last_name = last_name
    self.instruments = instruments
  
  def display(self):
    print('\nName: {} {}\nInstruments: {}'.format(self.first_name, self.last_name, ', '.join(self.instruments)))

if __name__ == "__main__":
  jerry = TalkingHead('Jerry', 'Harrison', ['Guitar', 'Keyboards', 'Vocals', 'Bass'])
  tina = TalkingHead('Tina', 'Weymouth', ['Bass', 'Vocals', 'Synthesizer', 'Guitar'])
  david = TalkingHead('David', 'Byrne', ['Vocals', 'Guitar', 'Keyboards'])
  chris = TalkingHead('Chris', 'Frantz', ['Drums', 'Percussion'])
  bernie = TalkingHead('Bernie', 'Worrell', ['Synthesizer'])
  
  jerry.display()
  tina.display()
  david.display()
  chris.display()
  bernie.display()

