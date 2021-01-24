class PlayList:
    def __init__(self, nome, filmes = []):
        self.nome = nome
        self.filmes = filmes

    def adicionar_filme(self, filme):
        if filme not in self.filmes:
            self.filmes.append(filme)

    def tenho_o_filme(self, filme):
        return filme in self.filmes

    def __getitem__(self, item):
        return self.filmes[item]


class Filme():
    def __init__(self, titulo, diretor):
        self.titulo = titulo
        self.diretor = diretor

    def __str__(self):
        return f'{self.titulo} - {self.diretor}'

    def __eq__(self, other):
        return self.titulo == other.titulo and self.diretor == other.diretor

    def __ne__(self, other):
        return self.titulo != other.titulo and self.diretor != other.diretor


playlist = PlayList('Minha Playlist')
playlist.adicionar_filme(Filme('A Teoria de Tudo', 'James Marsh'))
playlist.adicionar_filme(Filme('La La Land', 'Damien Chazelle'))
playlist.adicionar_filme(Filme('O Poderoso Chefão', 'Francis Ford Coppola'))

playlist.adicionar_filme(Filme('La La Land', 'Damien Chazelle'))
playlist.adicionar_filme(Filme('La La Land', 'Damien Chazellee'))

filme_procurado = Filme('La La Land', 'Damien Chazellee')
print(f'O filme ({playlist.tenho_o_filme(filme_procurado)}) na playlist')

for filme in playlist:
    print(filme)
