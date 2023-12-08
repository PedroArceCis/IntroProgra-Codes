###Item 1 (10ptos.)###

def initNotas(ramos):
    llave = {}
    for i in ramos:
        llave[i] = 0
    return (llave)
ramos = ("fis100","iwg101","tel101","mat021")
notas = initNotas(ramos)
#print(notas)



###Item 2 (50ptos.)###

def promNotas(notas):
    llavebacan = {}
    for i in notas:
        txt = i+".txt"
        try:
            arch = open(txt, "r")
        except OSError as err:
            print("El archivo "+txt+" no existe. Por favor, inténtelo nuevamente.")
            print(err, type(err))
            break #Esto porque encuentro inútil que la función siga trabajando si hay un error de apertura de archivo.
        else:
            notitas = 0
            cont = 0
            for a in arch:
                lista = a.split()
                num = int(lista[1])
                notitas += num
                cont += 1
            prom = notitas/cont
            notabacan = round(prom)
            llavebacan[i] = notabacan
            arch.close()
    return(llavebacan)
            
notas = promNotas(notas)
#print(notas)



###Item 3 (40ptos.)###

def reporteNotas(datos):
    from matplotlib import pyplot as plt
    notas = promNotas(datos)
    fig = plt.figure(dpi=100)
    ax = fig.add_subplot(444)
    cont=0
    y=[]
    etiquetas=[]
    orden=[]
    for i in notas:
        cont+=1
        etiquetas.append(i)
        orden.append(notas[i])
        y.append(notas[i])
    orden.sort()
    x = range(0, cont)
    sep=0.6
    ax.bar(x, y, sep, color="red")
    ax.set_xticks(x)
    ax.set_xticklabels(etiquetas)
    nueva_x = -1
    for i in notas:
        nueva_x+=1
        if notas[i]==orden[-1]:
            nueva_y=notas[i]
            ax.bar(nueva_x, nueva_y, sep, color="blue")
    ax.set_title("Promedio de ramos cursados en el semestre", fontsize=12, fontweight="bold")
    plt.axhline(y=100, linestyle="--")
    plt.show()
    return

ramos = ("fis100","iwg101","tel101","mat021")
notas = initNotas(ramos)
#reporteNotas(notas)
