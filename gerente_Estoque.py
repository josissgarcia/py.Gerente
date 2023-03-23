from gerente import Gerente

class GerenteEstoque(Gerente):
    def atribuir_tarefa(self):
        print("Atribuir 5(cinco) funcionários para checagem de estoque")
        self.numero_funcionario_disponivel -= 5
        

      
gerente_estoque = GerenteEstoque(15)
print(f'Quantidade de funcionários: {gerente_estoque.numero_funcionario_disponivel}')
gerente_estoque.atribuir_tarefa()
print(f'Saldo de funcionários disponíveis após a atribuição da terefa: {gerente_estoque.numero_funcionario_disponivel}')
        