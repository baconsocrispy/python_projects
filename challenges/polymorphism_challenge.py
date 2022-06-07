# create two classes that inherit from another class
# 1. each child should have at least two attributes
# 2. parent class should have at least one method
# 3. both child classes should utilize polymorphism on parent method
# 4. comment throughout
# 5. upload to github

# parent class
class Keyboard:
  def __init__(self, type, num_keys, brand):
    self.type = type
    self.num_keys = num_keys
    self.brand = brand

  # at least one method
  def display():
    print('\nType: {}\nBrand: {}\nNumber of Keys: '.format(self.type, self.brand, self.num_keys))
  
# child classes
class Synthesizer(Keyboard):
  model = ''
  oscillators = 0
  filter = ''

  # utilize polymorphism
  def display(self):
    print('\nBrand: {}\nModel: {}\nKeys: {}\nFilter: {}\nOscillators: {}'.format(self.brand, self.model, self.num_keys, self.filter, self.oscillators))

class Piano(Keyboard):
  pedals = 0
  color = ''
  size = ''

  # utilize polymorphism
  def display(self):
    print('\nType: {}\nSize: {}\nColor: {}\nPedals: {}'.format(self.type, self.size, self.color, self.pedals))

if __name__ == "__main__":
  prophet = Synthesizer('Electric', 60, 'Dave Smith Instruments')
  prophet.model = 'Prophet 08'
  prophet.oscillators = 8
  prophet.filter = 'Curtis Low Pass'

  grand = Piano('Acoustic', 88, 'Steinway')
  grand.pedals = 3
  grand.color = 'White'
  grand.size = 'Grand Piano'

  prophet.display()
  grand.display()