database: list = []

class Model:
  
  @classmethod
  def create(cls, **kwargs):
    print(kwargs)
    cls.__init__(cls, **kwargs)
  
  @classmethod
  def insert_data(cls):
    global database
    classname = cls.__name__
    if not database or not (data for data in database if classname not in data):
        database.append({
          classname: [
            {
              "name": cls.name_user,
              "password": cls.password_user
              }
          ]
        })
        return 'New data inserted.'
    for data in database:
      if classname in data:
        data[classname].append({
          "name": cls.name_user,
          "password": cls.password_user
          })
        return 'Data inserted in column {}.'.format(classname)
      