### Variables ###
'''
La nomenclatura correcta de
las variables es todo
en minusculas y separadas con
guion bajo
'''
my_variable = "My string variable"

print(my_variable)

my_int_variable = 5

print(my_int_variable)

my_bool_variable = False


# Concatenación de variables en un print
print(my_bool_variable, my_int_variable, my_variable)

#Ahora transformo una variable a una string con str()
# y lo muestro por consola con type()

my_int_variable_to_string = str(my_int_variable)
print(my_int_variable_to_string)
print(type(my_int_variable_to_string))

print('Este es el valor de:', my_bool_variable)

# Algunas funciones del sistema
print(len(my_variable)) # len() cuenta los caracteres de la variable

# Variables en una sola linea ¡cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Alexander", "Sanz", "Alex", 32
print("Me llamo: ", name, surname,"Mi edad es: ", age, "Y mi alias es: ", alias)

# Inputs: no es muy habitual el uso salvo q se 
# desarrolen aplicaciones de interaccion con terminal
first_name = input('What is your name: ')
age = input('How old are you? ')
print(first_name)
print(age)

# Forzamos el tipo
address: str = "Mi direccion"
print(type(address))

address = 32
print(address)

print(type(address)) # Cambio a tipo "int"