from gerente import Gerente

class GerenteRH(Gerente):
    def atribuir_tarefa(self):
        print("Atribuir 1(um) funcionário para admissão")
        self.numero_funcionario_disponivel -= 1
        
    def demitir_funcionario(self):
        self.numero_funcionario_disponivel -= 1
        
        
gerente_de_rh = GerenteRH(5)
print(gerente_de_rh.numero_funcionario_disponivel)
print("------------------")

gerente_de_rh.demitir_funcionario()
print(gerente_de_rh.numero_funcionario_disponivel)