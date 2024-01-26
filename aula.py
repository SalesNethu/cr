class Autor:
    def __init__(self,nome = str, idade = int, nacionalidade = str):
        self.nome = nome
        self.idade = idade
        self.nacionalidade = nacionalidade


class Livro:
    def __init__(self, titulo = str, autor = str, genero = str, qnt_paginas = int):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.qnt_paginas = qnt_paginas



autor1 = Autor(nome= "Jaspion", idade= 40, nacionalidade= "japonesa")
livro1 = Livro(titulo= "As cronicas de Jaspion", autor= autor1, genero= "ação")

print(livro1.titulo)
       
                