###Item A (20 Ptos.)

def leer_datos(archivo1, archivo2):
    try:
        arch1=open(archivo1, "r")
    except OSError as err:
        print("Error en la apertura del primer archivo", type(err))
        print(err.args, err, "\nPor favor, intente nuevamente.")
    else:
        try:
            arch2=open(archivo2, "r")
        except OSError as f:
            print("Error en la apertura del segundo archivo", type(f))
            print(f.args, f, "\nPor favor, intente nuevamente.")
        else:
            productos = []
            cant_vendidos = []
            precio = []
            tipo = []
            listafinal = []
            for i in arch1:
                a=i.split()
                productos.append(a[0])
                cant_vendidos.append(a[1])
            for lol in arch2:
                b=lol.split()
                precio.append(b[1])
                tipo.append(b[2])
            listafinal.append(productos)
            listafinal.append(cant_vendidos)
            listafinal.append(precio)
            listafinal.append(tipo)
            arch1.close()    
            arch2.close()
            return (listafinal)

L = leer_datos("ventas.txt", "datos.txt")
#print(L)

###Item B (50 Ptos.)

from matplotlib import pyplot as plt
def por_tipo(tipo_prod,datos):
    productos = datos[0]
    cant_vendidos = datos[1]
    precio = datos[2]
    tipo = datos[3]
    if tipo_prod not in tipo:
        raise ValueError("El producto ingresado no existe. Por favor, intente nuevamente.")
    vendidostrue = []
    preciosdeverdad = []
    for num in cant_vendidos:
        a = int(num)
        vendidostrue.append(a)
    for nums in precio:
        b = int(nums)
        preciosdeverdad.append(b)
    contador = -1
    ventas_totales = []
    for numero in preciosdeverdad:
        contador += 1
        cant = vendidostrue[contador]
        wena = numero*cant
        ventas_totales.append(wena)
    cont = -1
    productos_bacanes = []
    ventas_bacanes = []
    for typee in tipo:
        cont += 1
        if typee == tipo_prod:
            bacan = productos[cont]
            productos_bacanes.append(bacan)
            plata = ventas_totales[cont]
            ventas_bacanes.append(plata)
    largobacan = len(productos_bacanes)
            
    fig = plt.figure(figsize=[15,8], dpi=100)
    if tipo_prod == "Frutas_y_Verduras":
        tipo_prod = "Frutas y Verduras"
    if tipo_prod == "Carnes_y_Pescados":
        tipo_prod = "Carnes y Pescados"
    fig.suptitle("Ventas semanales de "+tipo_prod, fontsize=24, fontweight="bold")
    x = range(0, largobacan)
    plt.plot(x,ventas_bacanes,"bD--", markerfacecolor="red", lw=3, ms=14)
    plt.xticks(ticks=x, labels=productos_bacanes)
    plt.show()
    return
#por_tipo("Abarrotes", L)

###Item C (30 Ptos.)

def compara_tipo(datos):
    cant_vendidos = datos[1]
    precio = datos[2]
    tipos = datos[3]
    vendidostrue = []
    preciosdeverdad = []
    for num in cant_vendidos:
        a = int(num)
        vendidostrue.append(a)
    for nums in precio:
        b = int(nums)
        preciosdeverdad.append(b)
    contador = -1
    ventas_totales = []
    for numero in preciosdeverdad:
        contador += 1
        cant = vendidostrue[contador]
        wena = numero*cant
        ventas_totales.append(wena)
    
    tipos_reales = []
    for i in tipos:
        if i not in tipos_reales:
            tipos_reales.append(i)
                    
    contar = -1
    num = 0
    ventas_prod = []
    for i in tipos_reales:
        for j in tipos:
            contar += 1
            if i == j:
                num += ventas_totales[contar]
        ventas_prod.append(num)
        contar = -1
        num = 0
                
    money = 0
    for dinero in ventas_totales:
        money += dinero
    moneyperostring = str(money)
    
    mayor = ventas_prod.copy()
    mayor.sort()
    explotar = []
    for i in ventas_prod:
        if i == mayor[-1]:
            explotar.append(0.4)
        else:
            explotar.append(0)
            
    fig = plt.figure(dpi=100)
    ax1 = fig.add_subplot(321)
    ax1.set_title("Ventas semanales totales: "+moneyperostring, fontsize=18, fontweight="bold")
    ax1.pie(ventas_prod, explode=explotar, labels=tipos_reales, autopct="%.2f%%", shadow = True, startangle=10)
    ax1.axis("equal")
    plt.show()
    return

#compara_tipo(L)
























