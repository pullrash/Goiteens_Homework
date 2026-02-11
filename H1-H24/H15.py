cube = lambda x: x ** 3 
share = lambda a, b: a % b == 0
sered_aref = lambda x, y: (x+y)/2
from_celsia = lambda c: 9/5*c+32
from_ferengeit = lambda f: 5/9*(f-32)
hipotenuza = lambda x, y: (x ** 2 + y ** 2)**(1/2)
print(cube(5))
print(sered_aref(5,8))
print(from_celsia(100))
print(from_ferengeit(50))
print(hipotenuza(3,4))