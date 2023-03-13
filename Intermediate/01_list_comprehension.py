### List Comprehension ###


my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)


my_range = range(8)
print(my_range) # acá imprime el rango (0, 8)
print(list(my_range)) # acá imprime la lista [0, 1, ...]


my_list = [i for i in range(8)]
print(my_list)

my_list = [i + 1 for i in range(8)] # Suma 1 a cada elemento de la lista
print(my_list)

my_list = [i * 2 for i in range(8)] # Multiplica por 2 a cada elemento de la lista
print(my_list)

my_list = [i * i for i in range(8)] # Multiplica por sí mismo a cada elemento de la lista
print(my_list)

# Acá le aplico una función a la lista: 

def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in range(8)]
print(my_list)
