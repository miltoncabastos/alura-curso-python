from datetime import date, datetime, timedelta
from pytz import timezone
# import pytz

print('DATA ATUAL')
data_atual = date.today()
print(data_atual)
print('{}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year))
print(data_atual.strftime('%d/%m/%Y'))
print('')

print('DATA COMPLETA ATUAL')
data_completa_atual = datetime.now()
print(data_completa_atual)
print(data_completa_atual.strftime('%d/%m/%Y %H:%M:%S'))
print('')

print('DATA CONVERTIDA DE TEXTO')
data_string = '17/01/2020 23:31:15'
data_e_hora = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
print(data_e_hora)
print('')

print('DATA COM TIMEZONE')
data_completa_atual_para_teste_sao_paulo = datetime.now()
# diferenca = timedelta(hours = -3)
# print (f'Timedelta: {diferenca}')
fuso_horario = timezone('America/Sao_Paulo')
print(f'Fuso horário: {fuso_horario}')
data_e_hora_sao_paulo = data_completa_atual_para_teste_sao_paulo.astimezone(fuso_horario)
print(data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M'))
print('')

# print('PYTZ')
# for tz in pytz.all_timezones:
#     print(tz)

