class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
   
    @property
    def nome(self):
        return self._nome
   
    @nome.setter
    def nome (self,novo_nome):
        self._nome = novo_nome.title()
   
    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    def imprime(self):
        print(f'{self.nome} - {self.ano} - {self._likes} Likes')

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao
        self._likes = 0

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas
        self._likes = 0


vingadores = Filme('Vingadores - Guerra infinita', 2018, 160)
vingadores.dar_likes()

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()
atlanta.dar_likes()


filmes_e_series = [vingadores,atlanta]

for programa in filmes_e_series:
    programa.imprime()