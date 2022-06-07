# create two classes that inherit from another class
# 1. ensure each child has at least two of their own attributes
# 2. add comments throughout

# parent class
class Person:
  first_name = ''
  last_name = ''
  age = 0
  gender = ''

# child classes
class Musician(Person):
  instruments = []
  band = ''

class Doctor(Person):
  field = ''
  hospital = ''
  medical_school = ''

# create a tina weymouth object
tina = Musician()
tina.first_name = 'Tina'
tina.last_name = 'Weymouth'
tina.age = 71
tina.gender = 'F'
tina.instruments = ['Bass', 'Keyboards']
tina.band = 'Talking Heads'

print(tina.instruments)
