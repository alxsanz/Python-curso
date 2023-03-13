### Hnadling eceptions ###

numberOne = 5
numberTwo = 1

numberTwo = "1"


# try except
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
 
except:
    # Se ejecuta si se produce una excepción o sea cuando hay un fallo en 'try' de lo contrario no  
    print("Se ha producido un error") 

# try except else finally (else y finally son opcionales)
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
 
except:
    print("Se ha producido un error")    

else: # Se ejecuta si no se produce una excepción
    print("La ejecución continua correctamente") 

finally:# Se ejecuta siempre
    print("La ejecución continua")       
    
# Captura de excepciones por tipo de error #

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")

except ValueError:
    print("Se ha producido un ValueError")    
 
except TypeError: # Se ejecuta except SOLO con ese tipo de error, si pongo otro tipo se rompe nuevamente
    # Se ejecuta si se produce una excepción
    print("Se ha producido un TypeError")

# Captura de la información de la excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")

except ValueError as error:
    print(error)

except Exception as exception: # Se lee como excepción genérica en caso de que lo anterior no sea (ValueError)
    print(exception) 

   