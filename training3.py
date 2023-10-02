
import sympy as sy
from math import *

# f(x) = ax^n
# f´(x) = n*ax^(n-1)

print("\n")
formula = "f(x) = ax^n"
print(formula)

grad_der_funktion = int(input("Bestimme den höchsten Grad in f(x): "))
print("\n")
print("Die höchste Vielfachheit(Exponent), muss als erstes definiert werden.")
grad = grad_der_funktion
einzelstücke_funktion = 1
gesamt_funktion_visuell = "f(x) = "
gesamt_funktion = 0
x = sy.Symbol('x')

while einzelstücke_funktion <= grad_der_funktion:
    
    if einzelstücke_funktion > 1:
        gesamt_funktion_visuell += " + "

    a = str(input("Lege a für die Funktion f(x) " + str(grad) + ". grades fest: "))
    n = str(input("Lege n für die Funktion f(x) " + str(grad) + ". grades fest: "))
    print("\n")

    if a == "1" and n == "1":
        function1 = "x"
        gesamt_funktion_visuell += function1

    elif a == "1" and n != "1":
        function2 = "x^" + n
        gesamt_funktion_visuell += function2

    elif a != "1" and n == "1":
        function3 = a + "x"
        gesamt_funktion_visuell += function3

    elif a != "1" and n != "1":
        function4 = a + "x^" + n
        gesamt_funktion_visuell += function4

    gesamt_funktion += float(a) * x ** float(n)
    
    einzelstücke_funktion += 1

    grad -= 1

b = str(input("Lege b für f(x) fest: "))

if b > "0":
    gesamt_funktion_visuell += " + " + b

elif b < "0":
    gesamt_funktion_visuell += " " + b

gesamt_funktion += float(b)

print("\n")    
print(gesamt_funktion_visuell)
print("\n")
 
fx = gesamt_funktion
nullstellen = sy.solve(fx, x)
reelle_nullstellen = [nullstelle for nullstelle in nullstellen if nullstelle.is_real]

if reelle_nullstellen:
    x_Werte = 1
    for nullstelle in reelle_nullstellen:  
        print("x" + str(x_Werte) + " = " + str(nullstelle))
        x_Werte += 1

else:
    print("Die Funktion " + gesamt_funktion_visuell + " besitzt keine Nullstellen.")

print("\n")
