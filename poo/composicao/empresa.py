from funcionario import Funcionario

class Empresa:
  
  def __init__(self, nome_empresa: str):
    """Inicializa uma nova empresa"""
    self.nome_empresa: str = nome_empresa
    self.funcionarios: list = []
    

func1 = Funcionario('Lucas', 20, 'Desenvolvedor')
func2 = Funcionario('Lucas', 21, 'Desenvolvedor')
empresa1 = Empresa('Empresa')
empresa1.funcionarios.append(func1)
print(empresa1.funcionarios)
empresa1.funcionarios.append(func2)
print(empresa1.funcionarios)
