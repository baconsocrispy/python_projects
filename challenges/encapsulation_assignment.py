# Requirements
# 1. make use of a private attribute or function
# 2. make use of a protected attribute or function
# 3. create and object that makes use of protected & private
# 4. comment throughout

class EvilPolitician:
  def __init__(self):
    # protected variable
    self._secret_benefactor = 'Saudi Arabia'
    # private variable
    self.__mistress = 'Amber Waves'
  # private methods
  def get_mistress(self):
    print(self.__mistress)
  
  def set_mistress(self, new_mistress):
    self.__mistress = new_mistress

# EvilPolitician Object
john_politician = EvilPolitician()
print(john_politician._secret_benefactor)
john_politician.get_mistress()
john_politician.set_mistress('Becky Barnett')
john_politician.get_mistress()