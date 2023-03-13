### File handling ###

# .txt file

import os

txt_file = open("Intermediate/my_file.txt", "w+") # r+ abre un archivo para leer y escribir

txt_file.write("\nMi nombre es Alex\nMi apellido Sanz\n32 años\nMi lenguaje es python")
# print(txt_file.read()) # Leemos e imprimimos todo el documento.
# print(txt_file.read(15)) # Imprimimos solo los primeros 15 caracteres,
# si ya lo imprimimos completo imprimira 15 caracteres vacios.
print(txt_file.readline())
print(txt_file.readline())
for line in txt_file.readlines():
    print(line)  # Acá imprimiriamos la 3era y 4ta línea.

txt_file.write("\nTambién me gusta Kotlin") 
print(txt_file.readline())   

txt_file.close()

with open("Intermediate/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Swift")

#os.remove("Intermediate/my_file.txt")

# .json file  

import json

json.dump

json_file = open("Intermediate/my_file.json", "w+")

json_test = { # En los json las claves deben ser strings
    "name":"Alex",
    "surname":"Sanz",
    "age": 32,
    "language":["Python", "Swift", "Kotlin"],
    "website":"https://alex.dev"
}

json.dump(json_test, json_file, indent= 2)

json_file.close()
# Hace falta cerrar el documento para poder leerlo:
with open("Intermediate/my_file.json", "r+") as read_file:
    for line in read_file.readlines():
        print(line)
        
json_dict = json.load(open("Intermediate/my_file.json")) 
print(json_dict)       
print(type(json_dict))
print(json_dict["name"])


# .csv file

import csv

csv_file = open("Intermediate/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name","surname","age","language","website"])
csv_writer.writerow(["ale","sanz", 32, "Python","alex.com"])

csv_file.close()
 
with open("Intermediate/my_file.csv") as read_file:
    for line in read_file.readlines():
        print(line)
         
# xlsx file
# import xlrd # Debe instalarse el módulo

# xml file
import xml         