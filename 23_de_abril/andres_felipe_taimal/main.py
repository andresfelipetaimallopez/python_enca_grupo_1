'''realizar las importacionde las funciones segun 
las 4 variantes vistas
hacer print a la ejecucion de las funciones importadas'''

from operaciones import suma,resta
print(suma(10,30))
print(resta(50,15))

from operaciones import*
print(multiplicacion(6,9))

import operaciones as op
print(op.division(10,2))

from operaciones import divisin_piso
print(division_piso(2,19))

from operaciones import numero_aleatoro
print(numero_aleatorio())

from operaciones import *
print(moudlo(3,8))
