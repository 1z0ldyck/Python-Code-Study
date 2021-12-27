class Model:
  
  @classmethod
  def create(cls, **kwargs):
    print(kwargs)
    cls.__init__(cls, **kwargs)