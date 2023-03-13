### Functions ###

def my_function():
    print("Esto es una función")
    
my_function()    
my_function() 
my_function() 

def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values(45, 72)
    
sum_two_values("Soy ", "Alex")

def sum_two_values_with_return(first_value, second_value):
    return first_value + second_value

result = sum_two_values(1, 7)

print(result)
print(result)
print(result) # acá devuelve 'None'

my_result = sum_two_values_with_return(10, 8)

print(my_result) # => Aca devuelve un valor en consola

def print_name(name, surname):
    print(f"{name} {surname} ")
    
print_name("Alex", "Sanz")
print_name(surname= "Sanz", name="Alex") # Se muestra ordenado xq especifíco la variable


def print_name_default (name, surname, alias="sin alias"):
    print(f"{name} {surname} {alias} ")
    
print_name_default(surname= "Sanz", name="Alex")    

def print_texts (*text): # Poniendo el * tengo un num de parámetros dinámico
    print(text)

print_texts("hola")    
print_texts("Hola","koko", "chori", 456)

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())
        
print_upper_texts("Hola","koko", "chori")        