from collections.abc import Sized


class MinhaListagem(Sized):
    def __len__(self) -> int:
        pass

    def __init__(self, descricao):
        self.descricao = descricao

    def __str__(self):
        return self.descricao


lista = MinhaListagem("Teste")
print(lista)
