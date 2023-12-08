import math
print ("Programa de aplicación a la serie de Maclaurin.")
x = float(input("Ingrese un valor para x: "))
N = int(input("Ingrese nivel de precisión N: "))
izi = 0 #Resultado del easy mode.
med = 0 #Resultado del medium mode.
hard = 0 #Resultado del hard mode.
def fact_n(int): #Defino función para sacar factoriales en modo med y hard.
    num = 1
    while int != 1:
        num *= int
        int -= 1
    return (num)
print ("sen(x)= ", math.sin(x)) #Seno real de x.
if N == 0: #Acá dejo todos los sen como el mismo número al ser nvl de prec 0.
    print ("Easy mode aprox: sen(x)= ", x)
    print ("Medium mode aprox: sen(x) = ", x)
    print ("Hard mode aprox: mc_sen(x,N)= ", x)
elif N == 1:
#Nivel de precisión el cual no funciona correctamente con como maneje cada modo.
    izi = 0
    num_1 = (-1**N) #-1
    num_2 = x**(2*N+1) #x**3
    factfini = (2*N)+1 #3
    izi -= (num_1*num_2)/factfini
    print ("Easy mode aprox: sen(x)= ", izi)
    print ("Normal mode aprox: sen(x)= ", izi)
    print ("Hard mode aprox: mc_sen(x)= ", izi)
else: 
#Sistema principal, que va aproximándose cada vez mas al valor real del sen(x). 
#(En nivel 15 ya lo iguala practicamente).
    rango_N = range(1, N+7, 2)
    for i in rango_N:
        factorial = i #Pieza clave para sacar el facotorial de cada número.
        fact2 = i #Mi suma de las multiplicaciones para el factorial.
        while factorial != 1:
            fact2 *= factorial-1
            factorial -= 1
        if i in range(3, N+7, 4):
            fact2 *= -1
        izi += ((x**i)/(fact2))
    fact3 = (2*N)+1 #Mismo sistema de antes para sacar factorial del 2*N+1.
    factfini = (2*N)+1
    while fact3 != 1:
        factfini *= fact3-1
        fact3 -= 1
    num_1 = (-1)**N
    num_2 = x**(2*N+1)
    if fact2 <= -1: #Esto para establecer si la última operación se suma o resta.
        izi += (num_1*num_2)/factfini
    elif fact2 >= 1:
        izi -= (num_1*num_2)/factfini
    print ("Easy mode aprox: sen(x)= ", izi)
    for i in rango_N:
        a = fact_n(i) #Factorial de cada número dentro del rango.
        if i in range(3, N+7, 4):
            a *= -1
        med += (x**i)/a
    b = (2*N)+1
    num_1 = (-1)**N
    num_2 = x**(2*N+1)
    if a <= -1:
        med += (num_1*num_2)/(fact_n(b))
    elif a >= 1:
        med -= (num_1*num_2)/(fact_n(b))
    print ("Medium mode aprox: sen(x)= ", med)
    