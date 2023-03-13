### Modules ###

import my_module

# from 10_functions import sum_two_values => no funciona porqque el fichero functions arranca con un numero

my_module.sumValue(3, 5, 7)
my_module.printValue("Hola Phyton")

from my_module import sumValue, printValue

sumValue(1, 4, 5) # ahora importando solo una funcion no es necesario poner module.sum(...)

printValue("Hola Phyton")

import math # Módulo del sistema

print(math.pi)

print(math.pow(2, 8))


from math import pi as pi_value

print(pi_value)