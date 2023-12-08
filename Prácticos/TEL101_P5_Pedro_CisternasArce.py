#Easy Mode.
def get_palabras(archivo):
    try:
        archivito = open(archivo,"r")
    except OSError as err:
        print ("Se ha detectado un error en su archivo. Por favor, inténtelo nuevamente.\n",err)
    else:
        lectura = archivito.read()
        lista = lectura.split()
        archivito.close()
    return lista
easy = get_palabras("palabras.txt")
print(easy,"\n")

#Medium Mode.
def sorteo(pal,int):
    if int <= 0:
        raise ValueError("Su número no puede ser menor o igual a cero.")
    largo = len(pal)
    if int > largo:
        raise ValueError("Su número excede la cantidad de palabras disponibles en el archivo.")
    no_seleccionados = pal.copy()
    seleccionados = []    
    rangonum = range(0,int)
    from random import randint
    for i in rangonum:
        largocopia = len(no_seleccionados)
        ran = randint(0,largocopia-1)
        pop = no_seleccionados.pop(ran)
        seleccionados.extend([pop])
    listadelistas = [seleccionados, no_seleccionados]
    return listadelistas
med = sorteo(easy,5)
print (med,"\n")

#Hard Mode.
N = int(input("Ingrese un número de sorteos: "))
M = int(input("Ingrese número de palabras por sorteo: "))
try:
    sorteito = open("sorteo.txt", "w")
except OSError as err:
    print ("Necesita crear un archivo de texto para la realización de los sorteos.\n",err)
else:
    if (N <= 0) or (M <= 0):
        fail = "Error de tipo ’ValueError’ en la realización de los sorteos. Sus números no pueden ser menores o iguales a cero."
        sorteito.write(fail)
        sorteito.close()
        raise ValueError(fail)
    n_sorteos = range(1,N+1)
    from random import randint
    copiapal = easy.copy() #Literalmente la función *get_palabras* usada en el Easy Mode.
    for i in n_sorteos:
        str_n = str(i)
        sorteo_n = "Sorteo "+str_n
        sorteito.write(sorteo_n)
        if M > len(copiapal):
            fail = "Fin de sorteos. Este sorteo no pudo ser realizado por error de tipo ’ValueError’."
            sorteito.write("\n"+fail)
            sorteito.close()
            raise ValueError(fail)
        a = sorteo(copiapal,M)
        b = a[0]
        sorteadas = "\n"
        ult = (b[-1:-2:-1])
        ultima_pal = str(ult[0])
        for word in b:
            copiapal.remove(word)
            palabra_str = str(word)
            if palabra_str != ultima_pal:
                sorteadas += palabra_str+" - "
            elif palabra_str == ultima_pal:
                if i == N:
                    sorteadas += palabra_str
                elif i != N:    
                    sorteadas += palabra_str+"\n\n"
        sorteito.write(sorteadas)
        fin = sorteo_n+" efectuado correctamente."
        print (fin)
    sorteito.close()