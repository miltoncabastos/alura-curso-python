import playlist
import modelos

vingadores = modelos.Filme("Vingadores - Guerra Infinita", 2019, 160)
atlanta = modelos.Serie("Atlanta", 2018, 2)

programas = [vingadores, atlanta]
playlist = playlist.Playlist("miltão playlist", programas)

lost = modelos.Serie("Lost", 2010, 6)
playlist.add_programa(lost)

print(f'a playlist {playlist.nome} tem {len(playlist)} programas, são eles:')
for programa in playlist:
    print(programa)