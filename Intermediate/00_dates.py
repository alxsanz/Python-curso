### Dates ###

from datetime import datetime

now = datetime.now()

# Esto tambien puede ir dentro de una funcion como lo hacemos 
# a continuación...
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())
    
    
print_date(now)

timestamp = now.timestamp()

print(timestamp)


### creamos una fecha ###

year_2023 = datetime(2023, 1, 1) # mínima cantidad de información para que se imprima la fecha

print_date(year_2023)
    
from datetime import time

current_time = time(23, 4, 15) # solo para el tiempo

print(current_time.hour)
print(current_time.minute)
print(current_time.second)


from datetime import date

current_date = date.today() # solo para fechas

print(current_date.year)
print(current_date.month)
print(current_date.day)


current_date = date(current_date.year, current_date.month + 1, current_date.day)
# De esta forma podemos hacer operaciones con la fecha

print(current_date.month)

from datetime import timedelta # El timedelta nos va a servir para operar con diferentes fechas

diff = year_2023 - now

print(diff)

diff = year_2023.date() - current_date

print(diff) 

start_timedelta = timedelta(200, 100, 100, weeks = 10) # dias, segundos, milisegundo y semanas
end_timedelta = timedelta(300, 150, 120, weeks = 18)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)

"""
Timedelta es mas usado para representar tiempos absolutos,
no para fechas específicas
""" 