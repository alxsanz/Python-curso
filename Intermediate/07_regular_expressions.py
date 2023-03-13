### Regular expressions ###

import re

# match

my_string = "Esta es la lección número 7: Lección llamada sExpresiones Regulares"
my_other_string = "Esta no es la lección 6: Manejo de archivos"

match = re.match("Esta es la lección", my_string, re.I)
print(match)
start, end = match.span() # Establecemos la variable para el tramo de texto
print(my_string[start:end])  # Imprimimos solo ese texto

match = re.match("Esta no es la lección", my_other_string, re.I)
# if not(match == None): # Otra forma de comprobar el None
# if match != None: # Otra forma de comprobar el None
if match is not None:   
        print(match)
        start, end = match.span() 
        print(my_other_string[start:end])
 
 
print(re.match("Esta es la lección", my_other_string))
print(re.match("Expresiones Regulares", my_string)) # Acá me dice "None" porque busca desde el principio del string

# search

search = re.search("lección", my_string, re.I) # A dif del match, search busca en cualquier parte del texto
print(search)
start, end = search.span() 
print(my_string[start:end])

# findall

findall = re.findall("lección", my_string, re.I)
print(findall) # findall directamente muestra una lista de todas las repeticiones de la palabra

# split

split = re.split(":", my_string)  # split busca un patron o caracter para dividir
print(split)

# sub
# Solo tiene en cuenta el primer valor que encuentra
print(re.sub("Expresiones", "expresiones", my_string)) 
print(re.sub("es|es", "ES", my_string)) # Poniendo así cambia en todos lados


# Patterns

pattern = r"[lL]ección"
print(re.findall(pattern, my_string))

pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[a-z]"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\d" # No tiene en cuenta las letras, D mayus no muestra números.
print(re.findall(pattern, my_string))

pattern = r"[l].*" # Así muestra la 'l' y todo lo que le sigue.
print(re.findall(pattern, my_string))

# Ejemplo buscar email:

email = "alexsanz@alex.com"
# Con este patrón solo encontrará formatos de email:
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$" # El \. exceptua que el mail termine en punto.
                        # El símbolo $ indica que tendra en cuenta todo lo que le sigue al punto 
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

# Página regex101.com es para analizar expresiones regulares.