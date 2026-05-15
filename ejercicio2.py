num1 = int(input("Ingrese su edad"))

if num1 >= 70:
    print("Es un adulto mayor de la tercera edad")
elif num1 >= 40 :
    print("Persona mayor")
elif num1 >= 18:
    print("Es adulto")
else :
    print("es un niño")

if num1 >= 60 and num1 <= 100:
    print("es viejo pero no tanto")
elif num1 < 60 and num1 >=40:
    print("no esta nada viejo")
elif num1 < 40 and num1 >= 18:
    print("Es adulto")   
elif num1 <18 and num1 >= 10:
    print("Es adolecente")
else:
    print("es un niño")