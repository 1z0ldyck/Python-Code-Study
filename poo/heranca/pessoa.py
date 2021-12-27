from database import Model
import enum

"""
example_data = [{
  "Pessoa": [
    {
      
    }
  ]
  }]


"""

data_bank = []



class Pessoa(Model):
  
  name_user = ''
  password_user = ''
  
  def __init__(self, name, password):
    self.name_user = name
    self.password_user = password
    self.insert_data()
  
  @classmethod
  def insert_data(cls):
    global data_bank
    classname = cls.__name__
    if not data_bank or not (data for data in data_bank if classname not in data):
        data_bank.append({
          classname: [
            {
              "name": cls.name_user,
              "password": cls.password_user
              }
          ]
        })
        return 'New data inserted.'
    for data in data_bank:
      if classname in data:
        data[classname].append({
          "name": cls.name_user,
          "password": cls.password_user
          })
        return 'Data inserted in column {}.'.format(classname)
    
  
p1 = Pessoa.create(name='Lucas', password=123)
print(data_bank)
p2 = Pessoa.create(name='Marquinhos', password=123)
print(data_bank)


