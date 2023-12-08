###Item A (10 Ptos.)

def leer_datos(archivo):
    try:
        arch = open(archivo, "r")
    except OSError as err:
        print("Error en la apertura del archivo", type(err))
        print(err.args, err, "\nPor favor, intente nuevamente.")
    else:
        lista = []
        for i in arch:
            A = i.split()
            lista.append(A)
        arch.close()
        return (lista)
L = leer_datos("visitas.txt")
#print(L)


###Item B (40 Ptos.)

from matplotlib import pyplot as plt
def visitas_semanales(canal,datos):
    canales=[]
    numeritos=[]
    for i in datos:
        canales.append(i[0])
    if canal not in canales:
        raise ValueError("El canal introducido no existe o está mal escrito. Por favor, intente nuevamente.")
    pos = -1
    for channel in canales:
        pos += 1
        if channel == canal:
            break
    canalbacan = datos[pos]
    del canalbacan[0]
    for num in canalbacan:
        numeritos.append(num)
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    numeritosderial = []
    for i in numeritos:
        numeritosderial.append(int(i))


    fig = plt.figure(figsize=[15,8],dpi=100)
    ax = fig.add_subplot(222)
    x = range(0,7)
    sep = 0.3
    ax.bar(x, numeritosderial, sep, color='red')
    ax.set_xticks(x)
    ax.set_xticklabels(dias)
    ax.set_title("Visitas Semanales de "+canal)
    plt.ylabel("Visitas [en miles]")
    plt.xlabel("Días de la Semana")
    plt.show()
    return
#visitas_semanales("JaponConSalame",L)
#Da error con "JapónConSalame" por el tilde.


###Item C (50 Ptos.)
def visitas_canales(datos):
    lunes_jueves = []
    viernes_domingo = []
    canales = []
    rango1 = range(1,5)
    rango2 = range(5,8)
    for i in datos:
        canales.append(i[0])
        lista = []
        for num in rango1:
            lista.append(int(i[num]))
        lunes_jueves.append(lista)
        lista2=[]
        for num in rango2:
            lista2.append(int(i[num]))
        viernes_domingo.append(lista2)
    
    mayor = lunes_jueves.copy()
    mayor.sort()
    explotar = []
    cont=-1
    for i in canales:
        cont+=1
        if lunes_jueves[cont] == mayor[-1]:
            explotar.append(0.4)
        else:
            explotar.append(0)
            
    lunes_tot=0
    martes_tot=0
    miercoles_tot=0
    jueves_tot=0
    viernes_tot=0
    sabado_tot=0
    domingo_tot=0
    
    lunes=[]
    martes=[]
    miercoles=[]
    jueves=[]
    viernes=[]
    sabado=[]
    domingo=[]
    
    rangoA = range(0,21)
    cont=-1
    for num in rangoA:
        cont+=1
        lunes.append(num[cont])
        martes.append(num[cont+1])
        miercoles.append(num[cont+2])
        jueves.append(num[cont+3])
        lunes_tot+=num[0]
        martes_tot+=num[1]
        miercoles_tot+=num[2]
        jueves_tot+=num[3]
        
        
    for num in viernes_domingo:
        viernes.append(num[0])
        sabado.append(num[1])
        domingo.append(num[2])
        viernes_tot+=num[0]
        sabado_tot+=num[1]
        domingo_tot+=num[2]
        
    visitas_totA = [lunes_tot, martes_tot, miercoles_tot, jueves_tot]
    visitas_totB = [viernes_tot, sabado_tot, domingo_tot]
    visitas_tot1=[]
    visitas_tot2=[]
    
    for num in rangoA:
        visitas_tot1.append(lunes[num]+martes[num]+miercoles[num]+jueves[num])
        print(visitas_tot1)
        visitas_tot2.append(viernes[num]+sabado[num]+domingo[num])
    
    size=visitas_tot1
    fig1 = plt.figure(dpi=100)
    ax1 = fig1.add_subplot(1,1,1) 
    ax1.pie(size, explode=explotar, labels=canales, autopct="%.1f%%", shadow = True, startangle=0)
    
    
    
    
    
    
    
    
    
    
    
    plt.show()
    return
visitas_canales(L)
