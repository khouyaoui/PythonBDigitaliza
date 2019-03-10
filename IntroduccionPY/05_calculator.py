import math
print("Calculadora")
num1=int(input("Ingresa el primer numero: "))
num2=int(input("Ingresa el segundo numero: "))

print("1 ----------> realizar la suma")
print("2 ----------> realizar la división "+ "("+str(num1)+" entre "+str(num2)+")")
print("3 ----------> realizar la multiplicación")
print("4 ----------> realizar exponencial")
eleccion=input("Que deseas hacer? ")

if(eleccion=="1"):
    print("La suma es "+str((num1+num2)))
if(eleccion=="2"):
    print("La división es "+str(int(num1/num2)))
if(eleccion=="3"):
    print("La multiplicación es "+str(num1*num2))
if(eleccion=="4"):
    print("La exponencial es "+str(math.exp(num1)))