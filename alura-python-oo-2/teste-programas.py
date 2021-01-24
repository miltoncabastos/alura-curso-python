import modelos

filme = modelos.Filme("Vingadores - Guerra Infinita", 2019, 160)
serie = modelos.Serie("Atlanta", 2018, 2)

programas = [filme, serie]

for programa in programas:
    print(programa)
    print(repr(programa))
