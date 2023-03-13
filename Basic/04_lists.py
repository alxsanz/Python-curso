### Lists ### con CORCHEEETEEES [] !!!!!

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [23, 23, 23, 43, 66, 88, 94]

print(my_list)

print(len(my_list))

my_other_list = [32, 1.75, "Alex", "Sanz"]

print(my_other_list[-2])

# print(my_other_list[-5])
# print(my_other_list[4]) en ambos casos da error por exceder posicion

print(my_list.count(23)) # cuenta las veces que se repite un objeto

age, height, name, lastname = my_other_list

print(name)
# (name, lastname = my_other_list) asi da error
                #   se deben colocar todos los elementos
                
print(my_list + my_other_list)

#print(my_list - my_other_list) error

my_other_list.append("Argentina")
print(my_other_list)

my_other_list.insert(3, "verde")# 3 indice para colocar el objeto
print(my_other_list)

my_other_list[3] = "Azul" # cambio el contenido del indice 3
print(my_other_list)

my_list.remove(23) # solo elimina uno de los numeros, no todos los 23
                   # siempre ha de ser un dato conocido que se encuentre en la lista
print(my_list)

my_list.pop() # elimina el ultimo en la lista
print(my_list)

print(my_list.pop()) # el print del .pop() tmb saca el ultimo

print(my_list.pop(3)) # hace pop del indice ingresado

my_pop_element = my_list.pop(2)
print(my_pop_element)

del my_list[1] # borra por indice seleccionado
print(my_list)

my_list.insert(1, 34)

my_new_list = my_list.copy()

my_list.clear() # borra todo en la lista
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort() # ordena de menor a mayor salvo que le ponga
print(my_new_list) # un criterio de ordenamiento

print(my_new_list[1:3]) # imprime los objetos entre el indice 1 y el 3



'''
my_list = "Hola Python"
print(type(my_list)) Muestra en consola: <class 'str'>
Pyton es de tipado dinamico, en este caso la variable my_list
pasa a ser una string.
Para que sea una lista deberia poner de la siguiente forma:
my_list = ["Hola Python"] o my_list = list("Hola Python")

'''




