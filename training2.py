
print("\n")
a = str(input("Lege a für f(x) fest: "))
n = str(input("Lege n für f(x) fest: "))
b = str(input("Lege b für f(x) fest: "))

if a == "1" and n == "1" and b == "0":
    function1 = "x"
    print("f(x) = " + function1)

elif a == "1" and n == "1" and b != "0":
    function2 = "x" + "+" + b
    print("f(x) = " + function2)

elif a == "1" and n != "1" and b == "0":
    function3 = "x^" + n
    print("f(x) = " + function3)

elif a == "1" and n != "1" and b != "0":
    function4 = "x^" + n + "+" + b
    print("f(x) = " + function4)    

elif a != "1" and n == "1" and b == "0":
    function5 = a + "x"
    print("f(x) = " + function5)

elif a != "1" and n == "1" and b != "0":
    function5 = a + "x" + "+" + b
    print("f(x) = " + function5)

elif a != "1" and n != "1" and b == "0":
    function5 = a + "x^" + n
    print("f(x) = " + function5)    

else:
    function6 = a + "x^" + n + "+" + b
    print("f(x) = " + function6)
    
print("\n")
