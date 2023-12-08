### Easy Mode ###
def getSpotiPyInfo(filename):
    try:
        archivo = open(filename, "r")
    except OSError as err:
        print("Su archivo ha sufrido un error de apertura. Por favor, inténtelo nuevamente.\n")
        print(err, type(err))
    else:
        lista = []
        dicc = {}
        for i in archivo:
            a = i.strip()
            lista.append(a.split(","))
        for a in lista:
            dicc[a[0]]=[float(a[1]), float(a[2]), float(a[3])]
        archivo.close()
        return(dicc)

easy = getSpotiPyInfo("spotipyData.conf")
#print(easy)



### Medim Mode ###
def getGenresData(info, generos, dato="popularidad"):
    if type(info) != dict:
        raise ValueError("Usted ha ingresado un primer elemento que no corresponde a un diccionario. Por favor, intente nuevamente.")
    if (dato!="bailable") and (dato!="duracion") and (dato!="popularidad"):
        raise ValueError("Dato solicitado inexistente. Por favor, intentelo nuevamente")
    estilos=[]
    listafinal=[]
    for i in info:
        estilos.append(i)
    tuplita1 = tuple(generos)
    listafinal.append(tuplita1)
    numeritos=[]
    for music in tuplita1:
        if music not in estilos:
            raise ValueError("El género "+music+" no existe. Por favor, intente nuevamente.")
        nums = info[music]
        if dato == "bailable":
            numeritos.append(nums[0])
        if dato == "duracion":
            numeritos.append(nums[1])
        if dato == "popularidad":
            numeritos.append(nums[2])
    tuplita2 = tuple(numeritos)
    listafinal.append(tuplita2)
    return(listafinal)

med = getGenresData(easy, ["hip hop","korean pop","rap metal"], dato="duracion")
#print(med)



### Hard Mode ###
from matplotlib import pyplot as plt
def GenerosDatos(info, generos, dato="popularidad"):
    if (dato!="bailable") and (dato!="duracion") and (dato!="popularidad"):
        raise ValueError("Dato solicitado inexistente. Por favor, intentelo nuevamente")
    if dato == "popularidad":
        datitos = getGenresData(info, generos)
    if dato == "bailable":
        datitos = getGenresData(info, generos, dato="bailable")
    if dato == "duracion":
        datitos = getGenresData(info, generos, dato="duracion")
    if len(generos)==1:
        raise ValueError("Su lista ingresada necesita como mínimo 2 géneros para que los gráficos tengan sentido. Por favor, intente nuevamente.")
    
    largo = len(datitos[0])
    x = range(0,largo)
    y = datitos[1]
    orden = list(datitos[1])
    orden.sort()
    
    fig = plt.figure(dpi=100)
    ax1 = fig.add_subplot(4,5,1)
    ax1.set_title("Gráficos respectos al dato: <"+dato+">", fontsize=13, fontweight="bold")
    ax1.plot(x, y, '--', color="red")
    ax1.axis([0,largo-1,orden[0],orden[-1]])
    ax1.set_xticks(x)
    ax1.set_xticklabels(datitos[0])
    
    ax2 = fig.add_subplot(4,5,2)
    explotar = []
    for i in y:
        if i == orden[-1]:
            explotar.append(0.1)
        else:
            explotar.append(0)
    ax2.pie(y, explode=explotar, labels=datitos[0], autopct="%.1f%%", shadow = True, startangle=160)
    ax2.axis("equal")

    plt.show()
    return

#GenerosDatos(easy, ["hip hop","korean pop","rap metal"])

