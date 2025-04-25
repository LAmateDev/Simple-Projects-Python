# Crie uma classe chamada Produto com atributos: nome, preço e quantidade
# Metodo 1: Calcular valor total -> Preço * quantidade
# Metodo 2: Atualizar Quantidade -> atualixa da quantidade de produtos
# Desafio : crie objetos do tipo produto, atualize a qnt de cada um deles

class Produto():
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def atualiza_quantidade(self):
        nova_quantidade = int(input('Digite uma nova quantidade para o produto: '))
        self.quantidade = nova_quantidade
        return self.quantidade
    
    def calcula_valortot(self):
        total = self.preco * self.quantidade
        print(total)


p1 = Produto('Caneta', 2, 10)
p1.atualiza_quantidade()
p1.calcula_valortot()