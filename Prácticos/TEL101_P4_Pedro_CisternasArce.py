#Easy Mode.
def tiene_num(str):
    a = str
    lista = list(str)
    copia = lista.copy()
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if len(a) <= 1:
        a = ("Su contraseña es muy corta.")
    else:
        for i in lista:
            flag = i in nums
            if flag:
                break
            copia.remove(i)
        if len(copia) == 0:
            raise ValueError("Su contraseña no tiene números.")
    return (a)
    
S = tiene_num("Segura_123!")
print (S)

#Normal Mode.
def tiene_char(str):
    mins = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
    "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    mays = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
    "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    sp = [".", ",", "?", "!", "_", "-"]
    a = str
    lista = list(str)
    copia = lista.copy()
    for i in lista:
        flag = i in mins
        if flag:
            break
        copia.remove(i)
    if len(copia) == 0:
        raise ValueError("Su contraseña no tiene minúsculas.")
    copia = lista.copy()        
    for i in lista:
        flag = i in mays
        if flag:
            break
        copia.remove(i)
    if len(copia) == 0:
        raise ValueError("Su contraseña no tiene mayúsculas.")
    copia = lista.copy()
    for i in lista:
        flag = i in sp
        if flag:
            break
        copia.remove(i)
    if len(copia) == 0:
        raise ValueError("Su contraseña no tiene caracteres especiales.")
    return (a)
    
S = tiene_char("Segura_123!")
print (S)

#Hard Mode.
password = str(input("Ingrese su contraseña: "))
listacontra = list(password)
while len(listacontra) > -1:
    if len(listacontra) < 8:
        print ("Contaseña muy corta. Se necesitan al menos 8 caracteres.")
        password = str(input("Ingrese su contraseña: "))
        listacontra = list(password)
    while len(listacontra) >= 8:
        error = 0
        try:
            tiene_num(password)
        except ValueError as v:
            print (v,  "Por favor, intente nuevamente.")
            error += 1
            password = str(input("Ingrese su contraseña: "))
            listacontra = list(password)
        try:
            tiene_char(password)
        except ValueError as v:
            print (v, "Por favor, intente nuevamente.")
            error += 1
            password = str(input("Ingrese su contraseña: "))
            listacontra = list(password)
        else:
            if error >= 1:
                break
            elif error == 0:
                break
    if error == 0:
        print ("Contraseña registrada exitosamente.")
        break