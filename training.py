
import sympy as sy
from math import *

# f(x) = ax^n
# f´(x) = n*ax^(n-1)

print("\n")
formula = "f(x) = ax^n"
print(formula)

zusammengesetzte_funktionen = int(input("Wieviele Zusammengesetzte Funktionen insgesamt in f(x): "))
einzelfunktionen = 1
while einzelfunktionen <= zusammengesetzte_funktionen:
    
    a = str(input("Lege a für f(x) fest: "))
    n = str(input("Lege n für f(x) fest: "))
    b = str(input("Lege b für f(x) fest: "))
    
    einzelfunktionen += 1
    

a = str(input("Lege a für f(x) fest: "))
n = str(input("Lege n für f(x) fest: "))

if a == "1" and n == "1":
    function1 = "x"
    print("f(x) = " + function1)

elif a == "1":
    function2 = "x^" + n
    print("f(x) = " + function2)

elif n == "1":
    function3 = a + "x"
    print("f(x) = " + function3)

else:
    function4 = a + "x^" + n
    print("f(x) = " + function4)
    
print("\n")


x = sy.Symbol('x')
fx = x**2 - 2
nullstellen = sy.solve(fx, x) 
for nullstelle in nullstellen:
    print(float(nullstelle))
