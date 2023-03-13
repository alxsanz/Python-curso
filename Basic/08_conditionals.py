### Conditionals ###

my_condition = False

if my_condition: # Esto es lo mismo que escribir: if my_condition == true :
    print("Se ejecuta la condición del if")
    
       
my_condition = 3 * 9 # No determina nada solo es un valor, no es ni true ni false

if my_condition:
    print("Se ejecuta la condicion del segundo if") # Acá se ejecuta
    
if my_condition == 11:
    print("Se ejecuta la condicion del tercer if") # Este no se ejecuta debido a que
    # la condicion ya esta establecida, por lo que estamos obligando a comprobar algo en concreto
        
if my_condition == 27: # Ahora se ejecuta, cumple con el valor de la variable.
    print("Se ejecuta la condicion del 4to if")
            
if my_condition < 110:            
    print("Es un número mayor a 27")
         
else: 
    print("Es un número menor a 27")
    
if my_condition < 30 and my_condition > 10 :            
    print("Es un número menor que 30 y mayor a 10")    

elif my_condition == 1:
    print("es igual a 1")
        
        
print("La ejecución continua")        
        
    
my_string = ""
# Acá abajo no va a imprimir nada ya que un string vacío equivale a FALSE
if my_string:
    print("My cadena de texto es vacia") 


my_string = "Cadena de texto"

if my_string:
    print("My cadena de texto no es vacia") 
    
if my_string == "Cadena de texxxxtoooo":
    print("Estos se imprime si coincide el contenide de my_string") # En este caso no coincide
         
my_string = ""
# Ahora acá abajo si se imprime ya q el 'not' niega la condición de string vacía
if not my_string:
    print("My cadena de texto es vacia")          