# class Playlist:
#     def __init__(self, nome):
#         self.nome = nome
#         self.__programas = []
#
#     def adicionar_programa(self, programa):
#         self.__programas.append(programa)
#
#     def listar_programas(self):
#         for programa in self.__programas:
#             print(programa)
#
#     def tamanho(self):
#         return len(self.__programas)
#
#     def informacoes_playlist(self):
#         print(f'{self.nome} - com {self.tamanho()} programas')
#         self.listar_programas()

class Playlist():
    def __init__(self, nome, programas = []):
        self.nome = nome
        self.__programas = programas

    def add_programa(self, programa):
        self.__programas.append(programa)

    def __getitem__(self, item):
        return self.__programas[item]

    def __len__(self):
        return len(self.__programas)
