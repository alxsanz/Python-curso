### Python Package Manager ###

# PIP https://pypi.org

# Acá en windows para instalar modulos usamos: py -m pip install {módulo a instalar}

import numpy 

print(numpy.version.version)

numpy_array = numpy.array([22, 24, 26, 45, 78, 89])
print(type(numpy_array)) 

print(numpy_array * 2)

# import pandas

# pip list => en windows : py -m pip list
# pip uninstall pandas => py -m pip uninstall pandas
# pip show numpy => py -m pip show numpy

# pip install requests => esta libreria es para hacer peticiones a una api

import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json()) 

# Arithmetics package

from my_package import arithmetics

print(arithmetics.sum_two_values(2 , 5))