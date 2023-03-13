### Tuples ### CON PARENTESISSSSS () !!!!

my_tuple = tuple() # estas son las formas de
my_other_tuple = () # definir las tuplas

my_other_tuple = (32, 55, 70)

my_tuple = (32, 1.75, "Alex", "Sanz")
print(my_tuple)

print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[-1])

# my_tuple[1] = 1.80 Error: 'tuple' object does not support item assignment

"""
Las tuplas son listas inmutables,
puedo consultar indice, contar objetos, 
pero no permiten ningun tipo de alteracion
"""

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple) # de esta forma sumando otra variable puedo agregar datos

print(my_sum_tuple[4:6])# elementos entre el 4 y el 6

my_tuple = list(my_tuple)
print(type(my_tuple)) # se puede transformar en lista y visceversa en caso de ser necesario

del my_tuple #independientemente del tipo de variable, la acción
             # 'del' borrara toda la información de la misma
# print(my_tuple) Error: name 'my_tuple' is not defined


