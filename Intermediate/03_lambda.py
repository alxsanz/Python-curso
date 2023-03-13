### Lambdas ###

"""
Inicialmente se entiende a las lambdas como funciones
anónimas (sin nombre).
"""

sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(2, 4))


multiply_values = lambda first_value, second_value: first_value * second_value -2
print(multiply_values(3, 4))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

my_sum = sum_three_values(5)(3, 4)
print(my_sum)

#  ó también

print(sum_three_values(5)(2, 4))

