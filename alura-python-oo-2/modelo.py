class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas

filme = Filme("Vingadores - Guerra Infinita", 2019, 160)
print(f'{filme.nome}, lançado em {filme.ano} com duração de {filme.duracao} min')

serie = Serie("Atlanta", 2018, 2)
print(f'{serie.nome}, lançada em {serie.ano} com {serie.temporadas} temporadas')