import programa


class Filme(programa.Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome}, lançado em {self.ano} com duração de {self.duracao} min'


class Serie(programa.Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self.nome}, lançada em {self.ano} com {self.temporadas} temporadas'
