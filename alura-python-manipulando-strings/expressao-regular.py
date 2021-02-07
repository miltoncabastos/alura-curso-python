import re

email1 = 'Meu número é 1234-5678'
email2 = 'fale comigo em 12345678 esse é meu telefone'
email3 = '91234-5678 é o meu celular'
email4 = 'Meu telefone fixo é 12345678 é o meu celular é 91234-5678'

# padrao = "[0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789][0123456789][0123456789]"
padrao = '[0-9]{4,5}[-]*[0-9]{4}'

print('email1: ' + re.search(padrao, email1).group())
print('email2: ' + re.search(padrao, email2).group())
print('email3: ' + re.search(padrao, email3).group())
print('email4: ' + str(re.findall(padrao, email4)))