### Loops ### En español: bucles o ciclos.

"""

Iterar es básicamente repetir algo,
un bucle nos sirve para pasar por
un mismo código varias veces

"""

# Bucle : while 

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2 # Se pone esta condición para que no se 
                      # repita indefinidamente
else: # (opcional) Esto de meterle un else a un while no lo tienen varios lenguajes
    print("Mi condición es mayor o igual que 10")                      

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
        
    print(my_condition)


# Bucle: For

my_list = [23, 23, 23, 43, 66, 88, 94]

for element in my_list: # for hace una impresión x/c elemento de la lista    
    print(element)      # funciona tmb para sets, tuplas y diccionarios

my_dict = {"Nombre":"Alex", "Apellido":"Sanz", "Edad": 32, 1:"Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        print("Acá pasa la edad")
        continue

for element in my_dict.values(): # ahora se imprimen los valores
    print(element)    
       
print("La ejecución continua")                      
    

