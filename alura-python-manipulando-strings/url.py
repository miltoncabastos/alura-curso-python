
# argumento = 'http://www.bytebank.com.br/cambio?moedaorigem=real'
# substring = argumento[5:11]
# print(substring)

# argumento = 'moedaorigem=real'
# index = argumento.find('=') + 1
# print(index)
# substring = argumento[index:]
# print(substring)
# string_split = argumento.split('=')
# print(string_split)

# url = 'https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500'
# index_url = url.find('?') + 1
# argumentos = url[index_url:].split('&')
# for argumento in argumentos:
#     parametro = argumento.split('=')
#     variavel = parametro[0]
#     valor = parametro[1]
#     print(f'a variável ({variavel}) tem o valor ({valor})')

celular = '(47)96574-1728'
indiceInicialCodigoArea = celular.find("(")+1
indiceFinalCodigoArea = celular.find(")")
print(celular[indiceInicialCodigoArea:indiceFinalCodigoArea])
