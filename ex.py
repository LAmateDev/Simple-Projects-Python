# Crie uma classe chamada Livro com os seguintes atributos: Titulo, Autor, Numero de paginas
# Metodos: detalhes - imprime todos os atributos do livro

# Desafio
# Crie uma lista dos objetos de objetos de tipo livro e imprima os detalhes de cada um dele

class Livro():
    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas

    def detalhes(self):
         print(f"Nome do livro: {self.titulo}\nNome do autor: {self.autor}\nNúmero de páginas: {self.numero_paginas}")
    
livros = [Livro("Introdução a Programação com Python", "Nilo Ney", 323),
          Livro("Crime e Castigo", "DoisToiesk", 412),]

for livro in livros:
    livro.detalhes()
    print()    