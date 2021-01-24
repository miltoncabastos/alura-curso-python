class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_likes(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @classmethod
    def info(cls):
        print(f'informações da classe: {cls.likes}')

    def infoExternal(self):
        self.info()

    @staticmethod
    def infoStatic():
        print(f'informações estáticas da classe')