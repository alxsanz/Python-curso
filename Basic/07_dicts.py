### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

# Relación clave-valor:

my_other_dict = {"Nombre":"Alex", "Apellido":"Sanz", "Edad": 32, 1:"Python"}

my_dict = {
    "Nombre":"Alex",
    "Apellido":"Sanz",
    "Edad": 32,
    "lenguajes":{"Python", "React", "Kotlin"},
    1:1.75
    }


print(my_dict)
print(my_other_dict)
print(type(my_other_dict))
print(len(my_dict))


print(my_dict["Nombre"]) # Imprime: Alex

my_dict["Nombre"] = "Lex"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Calle Lex"
print(my_dict)

del my_dict["Calle"] # Así eliminamos un elemento del dict
print(my_dict)

print("Sanz" in my_dict) # Da False
print("Apellido" in my_dict) # Da True, solo encuentra claves de esta forma

# Para obtener el valor de la clave he de poner:
print(my_dict["Apellido"]) # => Muestra: Sanz

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso")) # Esta prop genera un dict sin claves, podria
print(my_new_dict)                                 # usar tanto dict.(p/crear diccionario genérico)
                                                   # como un diccionario ya creado
                                                   
                                                   
my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys(my_list) 
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, "Sin clave") # Aca se le pone lo mismo a todas las claves
print(my_new_dict)

print(list(my_new_dict)) # Imprime solo las claves una vez transformado en lista