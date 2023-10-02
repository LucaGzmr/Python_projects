
import sympy as sy
from math import *

# f(x) = ax^n
# f´(x) = n*ax^(n-1)

print("\n")
formula = "f(x) = ax^n"
print(formula)

x = sy.Symbol('x')
funktion = str(input("Gebe die Funktion f(x) für die Kurvendisskussion an: f(x) = "))
funktion = funktion.replace("^", "**")
print("\n")

fx = funktion
nullstellen = sy.solve(fx, x)
reelle_nullstellen = [nullstelle for nullstelle in nullstellen if nullstelle.is_real]

if reelle_nullstellen:
    x_Werte = 1
    for nullstelle in reelle_nullstellen:  
        print("x" + str(x_Werte) + " = " + str(nullstelle))
        x_Werte += 1

else:
    print("Die Funktion " + funktion + " besitzt keine Nullstellen.")

print("\n")
