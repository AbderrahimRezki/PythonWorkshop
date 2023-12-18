import math_functions
print(math_functions.add(343, 23))


# Using aliases
import math_functions as math_funcs
print(math_funcs.add(10, 20))

# from import
from math_functions import add, substract

print(add(1, 2))
print(substract(2, 3))

# from import using aliases
from math_functions import add as plus, substract as minus

print(plus(5, 3))
print(minus(5, 3))

# import everything
from math_functions import *