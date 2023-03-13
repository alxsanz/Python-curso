### Higher order functions ###

from functools import reduce # Es necesario importar esta función.

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5


def sum_two_values_and_add_one(first_value, second_value):
    return sum_one(first_value + second_value)

print(sum_two_values_and_add_one(2, 3))

# Ahora ponemos la letra "f" para agregar funciones unas dentro de otras

def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_add_value(2, 3, sum_one))
print(sum_two_values_and_add_value(2, 3, sum_five))

### Closures ###

def sum_ten():
    def add(value):
        return value + 10
    return add # esto es un closure


print(sum_ten()(25)) # esto es una función que retorna una función

add_closure = sum_ten() # esto es una función que retorna una función
print(add_closure(5))    

# Ahora con un value en sum_ten()
 
def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add # esto es un closure

add_closure = sum_ten(1) # esto es una función que retorna una función
print(add_closure(5))   

sum_ten(5)(1)
print(sum_ten(8)(7))

### Built-in Higher order functions ###

"""
Las funciones de orden superior pueden ejecutar otras funciones
"""

numbers = [2, 4, 5, 7, 23]

# Map


# Esta función siempre va a necesitar una lista iterable,
# es decir, un conjunto de valores, y que vamos a hacer con dicha lista.

def multiply_two(number):
    return number * 2

print(map(multiply_two, numbers)) # De esta forma imprime un objeto (object at 0x000001D8852D7FD0)
print(list(map(multiply_two, numbers))) # Así una lista: [4, 8, 10, 14, 46]
# Para c/valor de la lista "map" ejecutó la función que le pasamos.

print(list(map(lambda number: number * 2, numbers))) # Acá en una linea hacemos
# todo lo mismo con una función Lambda.

# Filter


# Como dice en su nombre, filter retorna los valores con
# true o false da la lista itarada.


def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(filter(filter_greater_than_ten, numbers)) # Genera un objeto.
print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers))) # Se muestra la lista.

# Reduce

# Reduce recorre la lista uno a uno operando con cada valor mas el acomulado.

def sum_two_values(first_value, second_value):   
        print(first_value)
        print(second_value)
        return first_value + second_value

numbers = [2, 4, 5, 7, 23]

print(reduce(sum_two_values, numbers)) # Imprime => 2, 4, 6, 5, 11, 7, 18, 23, 41
    
    
    
    
    
    
    
    
    