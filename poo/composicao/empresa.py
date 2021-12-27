class Empresa:
  
  __funcionarios = []
  
  def __init__(self, nome_empresa: str, qt_funcionarios: int):
    """Inicializa uma nova empresa"""
    self.nome_empresa = nome_empresa
    self.qt_funcionarios = qt_funcionarios
    
  @property
  def funcionarios(self):
    """Obtém os funcionários do momento."""
    return self.__funcionarios

  @funcionarios.setter
  def funcionarios(self, funcionario):
    """Adiciona um novo funcionário caso a quantidade de funcionários não estiver no limite."""
    if(self.qt_funcionarios == len(self.__funcionarios)):
      return False
    self.__funcionarios.append(funcionario)
    
from funcionario import Funcionario

func1 = Funcionario('Lucas', 20, 'Desenvolvedor')
func2 = Funcionario('Lucas', 21, 'Desenvolvedor')
empresa1 = Empresa('Empresa', 1)
empresa1.funcionarios.append(func1)
print(empresa1.funcionarios)
print(empresa1.funcionarios.append(func2))
