from ExtratorArgumentosUrl import ExtratorArgumentoUrl

url = "https://bytebank.com/cambio?moeDaorigem=real&moedadestino=dolar&valor=700"
# url = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=700"
# url = 0
extrator = ExtratorArgumentoUrl(url)
print(f'URL: {extrator.url}')

argumento = "moedaorigem"
print(f'Moeda Origem: {extrator.extrairArgumentos(argumento)}')

argumento = "moedadestino"
print(f'Moeda Destino: {extrator.extrairArgumentos(argumento)}')

argumento = "valor"
print(f'Valor: {extrator.extrairArgumentos(argumento)}')