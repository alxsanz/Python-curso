### Strings ###

my_string = "Mi string"
my_other_string = "Mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = " Esto es un string\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)

my_string_null = "\\n ahora esto no tiene efecto\\t con doble barra"


# Formateo

print("Mi nombre es Alex Sanz")

name, surname, age = "Alex", "Sanz", 32

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))

print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
# Esta para especificar el formato de datos ↑↑↑
print(f"Mi nombre es {name} {surname} y mi edad es {age}")# Inferencia de datos
# esta es la forma mas recomendada(rápida) ↑↑↑

# Desempaquetando caracteres

language = "Python"

a, b, c, d, e, f = language

print(a)
print(e)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-3]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

pto = language[0:6:2] # 2 es el paso en letras q va evitando
# P=si, y=no, t=si ... de la posición 0 a la 6ta.
print(pto) # imprime 

# Funciones

print(language.capitalize()) # primera letra en mayúscula
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("Py"))