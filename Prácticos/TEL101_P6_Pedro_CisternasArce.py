### Beginner Mode. ###
def leer_datos(archivo):
    try:
        arch = open(archivo, "r")
    except OSError as err:
        print("Ha surgido un error para abrir su archivo", type(err))
        print(err.args, err, "\nPor favor, intente nuevamente.")
    else:
        lista = []; generos = []; edad = []
        apruebo_rechazo = []; mixta_cnst = []
        for line in arch:
            a = line.split(";")
            generos.append(a[0])
            edad.append(a[1])
            apruebo_rechazo.append(a[2])
            no_n = a[3].strip()
            mixta_cnst.append(no_n)
        lista.append(generos)
        lista.append(edad)
        lista.append(apruebo_rechazo)
        lista.append(mixta_cnst)
        arch.close()
        return (lista)
lectura = leer_datos("encuesta.txt")
#print(lectura)



### Easy Mode. ###
from matplotlib import pyplot as plt
def generales(preg1, preg2):
    apruebo = 0; rechazo = 0; mixta = 0; constitucional = 0
    for i in preg1:
        if i == "1":
            apruebo += 1
        if i == "2":
            rechazo += 1
    for i in preg2:
        if i == "1":
            mixta += 1
        if i == "2":
            constitucional += 1
    etiquetas = ["Apruebo", "Rechazo"]
    size = [apruebo, rechazo]
    colores = ["limegreen", "firebrick"]
    fig = plt.figure(dpi=100)
    ax1 = fig.add_subplot (3,3,1) 
    ax1.pie(size, labels=etiquetas, colors=colores, autopct="%.1f%%", startangle=350)
    ax1.axis("equal")
    ax1.set_title("¿Quiere usted una Nueva Constitución?", fontsize=12, fontweight="bold")
    etiquetas2 = ["Convención Mixta", "Convención Constitucional"]
    size2 = [mixta, constitucional]
    ax2 = fig.add_subplot(3,3,2) 
    colores2 = ["orangered", "dodgerblue"]
    ax2.pie(size2, labels=etiquetas2, colors=colores2, autopct="%.1f%%", startangle=260)
    ax2.axis("equal")
    ax2.set_title("¿Qué tipo de órgano debería redactar la Nueva Constitución?", fontsize=12, fontweight="bold")
    plt.show()
    return
#generales(lectura[2], lectura[3])



### Medium Mode. ###
def votos_genero(genero, preg1, preg2):
    apruebo_F = 0; rechazo_F = 0; mixta_F = 0; const_F = 0
    apruebo_M = 0; rechazo_M = 0; mixta_M = 0; const_M = 0
    cont = -1
    for gen in genero:
        cont += 1
        if gen == "F":
            if preg1[cont] == "1":
                apruebo_F += 1
            if preg1[cont] == "2":
                rechazo_F += 1
            if preg2[cont] == "1":
                mixta_F += 1
            if preg2[cont] == "2":
                const_F += 1
        if gen == "M":
            if preg1[cont] == "1":
                apruebo_M += 1
            if preg1[cont] == "2":
                rechazo_M += 1
            if preg2[cont] == "1":
                mixta_M += 1
            if preg2[cont] == "2":
                const_M += 1
                
    fig = plt.figure(dpi=100)
    
    #Desde acá me volé y se me olvidaron las existencias de los títulos y subtítulos por gráfico jaja xd
    #La vdd lo podría borrar y solo usar el .title pero como funciona con el mismo objetivo... Perdóneme la vida profe, si igual quedó decente ;-;
    ax1 = fig.add_subplot(432)
    if apruebo_F > rechazo_F:
        ax1.text(-7.5, apruebo_F*1.1, "Mujeres.", fontsize=22, fontweight="bold")
        ax1.text(-2, apruebo_F*1.1, "¿Quiere usted una Nueva Constitución?", color="#1e1e21", fontsize=13, fontweight="bold")
    else:
        ax1.text(-7.5, rechazo_F*1.1, "Mujeres.", fontsize=22, fontweight="bold")
        ax1.text(-2, rechazo_F*1.1, "¿Quiere usted una Nueva Constitución?", color="#1e1e21", fontsize=13, fontweight="bold")
    ax1.text(1.2,apruebo_F, str(apruebo_F)+" votos", color="#1b1b1c", fontsize=10)
    ax1.text(5.2,rechazo_F, str(rechazo_F)+" votos", color="#1b1b1c", fontsize=10)
    fig.subplots_adjust(top=0.95)
    sep = 1.5
    x = range(0,9)
    y = [0, 0, apruebo_F, 0, 0, 0, rechazo_F, 0, 0]
    ax1.bar(x, y, sep, color="#e8d717")
    ax1.set_xticks([2,6])
    ax1.set_xticklabels(["Apruebo", "Rechazo"])
    
    ax2 = fig.add_subplot(433)
    if mixta_F > const_F:
        ax2.text(-2, mixta_F*1.1, "¿Qué tipo de órgano debería redactar la Nueva Constitución?", color="#1e1e21", fontsize=13, fontweight="bold")
    else:
        ax2.text(-2, const_F*1.1, "¿Qué tipo de órgano debería redactar la Nueva Constitución?", color="#1e1e21", fontsize=13, fontweight="bold")
    ax2.text(1.2,mixta_F, str(mixta_F)+" votos", color="#1b1b1c", fontsize=10)
    ax2.text(5.2,const_F, str(const_F)+" votos", color="#1b1b1c", fontsize=10)
    y = [0, 0, mixta_F, 0, 0, 0, const_F, 0, 0]
    ax2.bar(x, y, sep, color="#e8d717")
    ax2.set_xticks([2,6])
    ax2.set_xticklabels(["Convención Mixta", "Convención Constitucional"])
    
    ax3 = fig.add_subplot(435)
    if apruebo_M > rechazo_M:
        ax3.text(-7.5, apruebo_M*1.1, "Hombres.", fontsize=22, fontweight="bold")
        ax3.text(-2, apruebo_M*1.1, "¿Quiere usted una Nueva Constitución?", color="#1e1e21", fontsize=13, fontweight="bold")
    else:
        ax3.text(-7.5, rechazo_M*1.1, "Hombres.", fontsize=22, fontweight="bold")
        ax3.text(-2, rechazo_M*1.1, "¿Quiere usted una Nueva Constitución?", color="#1e1e21", fontsize=13, fontweight="bold")
    ax3.text(1.2,apruebo_M, str(apruebo_M)+" votos", color="#1b1b1c", fontsize=10)
    ax3.text(5.2,rechazo_M, str(rechazo_M)+" votos", color="#1b1b1c", fontsize=10)
    y = [0, 0, apruebo_M, 0, 0, 0, rechazo_M, 0, 0]
    ax3.bar(x, y, sep, color="#7adb4d")
    ax3.set_xticks([2,6])
    ax3.set_xticklabels(["Apruebo", "Rechazo"])
    
    ax4 = fig.add_subplot(436)
    if mixta_M > const_M:
        ax4.text(-2, mixta_M*1.1, "¿Qué tipo de órgano debería redactar la Nueva Constitución?", color="#1e1e21", fontsize=13, fontweight="bold")
    else:
        ax4.text(-2, const_M*1.1, "¿Qué tipo de órgano debería redactar la Nueva Constitución?", color="#1e1e21", fontsize=13, fontweight="bold")
    ax4.text(1.2, mixta_M, str(mixta_M)+" votos", color="#1b1b1c", fontsize=10)
    ax4.text(5.2, const_M, str(const_M)+" votos", color="#1b1b1c", fontsize=10)
    y = [0, 0, mixta_M, 0, 0, 0, const_M, 0, 0]
    ax4.bar(x, y, sep, color="#7adb4d")
    ax4.set_xticks([2,6])
    ax4.set_xticklabels(["Convención Mixta", "Convención Constitucional"])
    
    plt.show()
    return
#votos_genero(lectura[0], lectura[2], lectura[3])
    


### Hard Mode. ###
def votos_edad(edades, preg1, preg2):
    apruebo1=0;apruebo2=0;apruebo3=0;apruebo4=0
    rechazo1=0;rechazo2=0;rechazo3=0;rechazo4=0
    mixta1=0;mixta2=0;mixta3=0;mixta4=0
    const1=0;const2=0;const3=0;const4=0
    cont=-1
    for edad in edades:
        cont+=1
        if edad == "1":
            if preg1[cont]=="1":
                apruebo1+=1
            if preg1[cont]=="2":
                rechazo1+=1
            if preg2[cont]=="1":
                mixta1+=1
            if preg2[cont]=="2":
                const1+=1
        if edad == "2":
            if preg1[cont]=="1":
                apruebo2+=1
            if preg1[cont]=="2":
                rechazo2+=1
            if preg2[cont]=="1":
                mixta2+=1
            if preg2[cont]=="2":
                const2+=1
        if edad == "3":
            if preg1[cont]=="1":
                apruebo3+=1
            if preg1[cont]=="2":
                rechazo3+=1
            if preg2[cont]=="1":
                mixta3+=1
            if preg2[cont]=="2":
                const3+=1
        if edad == "4":
            if preg1[cont]=="1":
                apruebo4+=1
            if preg1[cont]=="2":
                rechazo4+=1
            if preg2[cont]=="1":
                mixta4+=1
            if preg2[cont]=="2":
                const4+=1
    plt.figure(figsize=[8,4.5],dpi=100)
    x = range(0,4)
    y1 = [apruebo1, apruebo2, apruebo3, apruebo4]
    plt.plot(x, y1, 'ko--', markerfacecolor="green", lw=1.5, ms=8, label="Apruebo")
    y2 = [rechazo1, rechazo2, rechazo3, rechazo4]
    plt.plot(x, y2, "ko--", markerfacecolor="red", lw=1.5, ms=8, label="Rechazo")
    y3 = [mixta1, mixta2, mixta3, mixta4]
    plt.plot(x,y3,"h-.", color="#380066", markerfacecolor="#00a398", lw=1, ms=7, label="Convención Mixta")
    y4 = [const1, const2, const3, const4]
    plt.plot(x,y4,"h-.", color="#380066", markerfacecolor="#ff7b00", lw=1, ms=7, label="Convención Constitucional")
    plt.xlabel("Rangos de edad")
    plt.ylabel("N° de votos")
    plt.suptitle("¿Quiere usted una Nueva Constitución?", fontsize=14, fontweight="bold")
    plt.title("¿Qué tipo de órgano debería redactar la Nueva Constitución?", color="#380066", fontsize=12, fontweight="bold")
    plt.xticks(ticks=x, labels=["18-30 años", "31-45", "45-65", "+65 años"])
    x=0
    for voto in y1:
        plt.text(x-0.1,voto-0.2,str(voto), color="green", fontsize=7)
        x += 1
    x=0
    for voto in y2:
        plt.text(x-0.1,voto-0.2,str(voto), color="red", fontsize=7)
        x += 1
    x=0
    for voto in y3:
        plt.text(x-0.1,voto-0.3,str(voto), color="#00a398", fontsize=7)
        x += 1
    x=0
    for voto in y4:
        plt.text(x-0.1,voto-0.3,str(voto), color="#ff7b00", fontsize=7)
        x += 1
    plt.legend()
    plt.show()
    return
#votos_edad(lectura[1], lectura[2], lectura[3])

