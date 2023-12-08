n1 = 0
n2 = 0
n3 = 0
n4 = 0
def nueva_apuesta(archivo):
    apuesta = open(archivo, "a")
    try:
        num1 = int(input("Ingrese un numero entre 1 y 30: "))
        if (num1<1) or (num1>30):
            raise ValueError("Su numero no esta permido. Por favor, intentelo nuevamente.")
        n1+=num1    
    except ValueError as e:
        print (e)
    else:
        num_str = str(num1)
        escribir = "\n"+num_str
        apuesta.write(escribir)
        try:
            num2 = int(input("Ingrese un numero entre 1 y 30: "))
            if (num2<1) or (num2>30):
                raise ValueError("Su numero no esta permido. Por favor, intentelo nuevamente.")
            if num2 == num1:
                raise ValueError("No puede repetir un numero. Por favor, intentelo nuevamente.")
            n2+=num2    
        except ValueError as a:
            print (a)
        else:
            num_str = str(num2)
            escribir = " "+num_str
            apuesta.write(escribir)
            try:
                num3 = int(input("Ingrese un numero entre 1 y 30: "))
                if (num3<1) or (num3>30):
                    raise ValueError("Su numero no esta permido. Por favor, intentelo nuevamente.")
                if (num3==num1) or (num3==num2):
                    raise ValueError("No puede repetir un numero. Por favor, intentelo nuevamente.")
                n3+=num3
            except ValueError as b:
                print (b)
            else:
                num_str = str(num3)
                escribir = " "+num_str
                apuesta.write(escribir)
                try:
                    num4 = int(input("Ingrese un numero entre 1 y 30: "))
                    if (num4<1) or (num3>30):
                        raise ValueError("Su numero no esta permido. Por favor, intentelo nuevamente.")
                    if (num4==num1) or (num4==num2) or (num4==num3):
                        raise ValueError("No puede repetir un numero. Por favor, intentelo nuevamente.")
                    n4+=num4   
                except ValueError as c:
                    print (c)
                else:
                    num_str = str(num4)
                    escribir = " "+num_str
                    apuesta.write(escribir)
    apuesta.close()
nueva_apuesta("apuestas.txt")

sorteos =  [[5 ,6 ,14 ,21] ,[2 ,4 ,6 ,8] ,[10 ,20 ,30 ,40] ,[1 ,3 ,12 ,25]]
comodines = [20 ,10 ,15 ,9]
str1 = str(n1)
str2 = str(n2)
str3 = str(n3)
str4 = str(n4)
apuesta = [str1, str2, str3, str4]
def resultados(apuesta, sorteos, comodines):
    resultadosfinalesfinales = []
    for i in sorteos:
        sorteito = i
        lista = []
        for numero in sorteito:
            strnum = str(numero)
            lista.append(strnum)
            for n in apuesta:
                resultadosfinales = []
                chinchin = 0
                if n in lista:
                    chinchin += 1
                resultadosfinales.append(chinchin)
        resultadosfinalesfinales += resultadosfinales
    return (resultadosfinalesfinales)    
print (resultados(apuesta,sorteos,comodines))
    