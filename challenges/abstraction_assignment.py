# Requirements:
# create a class that utilizes the concept of abstraction
# 1. your class should contain abstract and regular methods
# 2. create a child class the defines the implementation of parent's abstract method
# 3. create an object that utilizes both parent and child methods
# 4. add comments throughout your code

class LifeForm:
  breathing_apparatus = ''
  alive = True
  # abstract method
  def breathes(self):
    pass
  # regular method
  def dies(self):
    self.alive = False
    print('The {} is dead now...'.format(type(self).__name__.lower()))

class Fish(LifeForm):
  breathing_apparatus = 'gills'

  # child implements parent abstract class
  def breathes(self):
    print('The fish takes a breath through its {}'.format(self.breathing_apparatus))

# object uses parent & child methods
nemo = Fish()
nemo.breathes()
nemo.dies()



