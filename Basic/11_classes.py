### Classes ###

class MyEmptyPerson: # X buenas practicas las clases las escribimos con CamelCase
    pass # Cuando no queremos ejecutar nada en clases o funciones usamos 'pass'
         # Para que no tire error

# Podemos llamar a una clase con el paréntesis o sin el da igual 
print(MyEmptyPerson)
print(MyEmptyPerson())# Cuando se necesite ejecutar algo seran necesarios los paréntesis

class Person:
    def __init__(self, name, surname, alias = 'Sin alias'): # CONSTRUCTOR => Con esto 'Person' puede recibir paramentros
        self.name =  name
        self.surname = surname
        self.full_name = f"{name} {surname} {(alias)}" # Propiedad pública
        self.__name = name # Propiedad privada
    def get_name (self):
        return self.__name
        
    def walk(self):
        print(f"{self.full_name} está caminando")
    
    
    
    
my_person = Person("Alex", "Sanz")
print(my_person.name)    
print(f"{my_person.name} {my_person.surname}")
print(my_person.full_name)

my_person.walk()

my_other_person = Person("Gonzalo", "Higuaín", "Pipita")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "El Pipa Higuaín" # Ahora a full_name se le asigna una cadena de texto
print(my_other_person.full_name)

my_other_person.full_name = 666 # Ahora full_name es in int
print(my_other_person.full_name)