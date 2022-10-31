# http://docs.python.org/3.0/library/datetime.html
import calendar
from datetime import datetime, timedelta

data = datetime(2022, 10, 30, 10, 53, 20)  # inicializando data
data = datetime.strptime('28/04/2019', '%d/%m/%Y')  # str -> data

print(data)  # padrao é o americano
print(data.strftime('%d/%m/%Y %H:%M:%S'))  # formatar datas

data = data.timestamp()  # contagem de segundos
data = datetime.fromtimestamp(data)  # timestamp -> data
print(data)
print("----- separador -----")

data1 = datetime(2022, 10, 30, 21, 30, 20)
data2 = datetime(2021, 12, 2)
data2 = data2 + timedelta(days=5)
dif = data1 - data2

print(data1)
print(data2)
print(dif)
print("----- separador -----")

from locale import setlocale, LC_ALL
from calendar import monthrange

setlocale(LC_ALL, 'pt_BR.utf-8')
data_atual = datetime.now()
formatacao = data_atual.strftime('%A, %d de %B de %Y as %H:%M:%S')
year = int(data_atual.strftime("%Y"))
month = int(data_atual.strftime("%m"))
semana_ano = data_atual.isocalendar().week
diaI_diaF = monthrange(year, month)
print(formatacao)
print(f'semana {semana_ano} o mes tem {diaI_diaF[1]} dias')



