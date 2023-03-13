### Sets ### se denominan con llaves {}

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Alex", "Sanz", 32}

print(type(my_other_set))
print(len(my_other_set))

# print(my_other_set[0]) da error != de lista
# ya que los sets NO son estructuras ordenadas

my_other_set.add("verde")
print(my_other_set) # Imprime los datos revueltos

# Iinternamente el set utiliza un Hash para meter todos los elementos

my_other_set.add("verde") # Vuelvo a agregar "verde"
print(my_other_set) # Solo imprime un verde

# Un set no admite datos repetidos

# Para comprobar si un dato existe en el set:
print("Sanz" in my_other_set) # Da true
print("sanz" in my_other_set) # Da false

my_other_set.remove("verde")
print(my_other_set)

my_other_set.clear()
print(my_other_set)

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {"Alex", "Sanz", 32}
my_list = list(my_set) # La lista creada a partir del set ahora 
print(my_list)         # aparece de forma desordenada

print(my_list[0])

my_other_set = {"Html", "React", "Python"}
my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_new_set.union(my_new_set)) # Imprime lo mismo pues no se repiten elementos
print(my_new_set.union(my_new_set).union({"C++", "JavaScript"}))

print(my_new_set.difference(my_set))

