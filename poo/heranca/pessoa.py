"""Module Pessoa"""
from database import Model, database
import enum

"""
example_data = [{
  "Pessoa": [
    {
      
    }
  ]
  }]


"""


class Pessoa(Model):
  """Class for generating Pessoa"""
  
  name_user = ''
  password_user = ''
  
  def __init__(self, name, password):
    self.name_user = name
    self.password_user = password
    self.insert_data()
    

p1 = Pessoa.create(name='Lucas', password=123)
p2 = Pessoa.create(name='Marquinhos', password=123)
print(database)


