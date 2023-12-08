#Control 3 P201 (Pykadex).

#Item A.
def pykas_tipo(tipo, archivo):
    Flag = True
    while Flag:
        try:
            arc = open(archivo, "r")
        except BaseException as err:
            print("Lo sentimos, su archivo ha sufrido el siguiente error:\n", err)
            print ("\nPor favor, intententelo nuevamente.")
            break
        else:
            Flag = False
            pkmn = []
            for line in arc:
                a = line.split(",")
                if tipo in a:
                    pkmn.append(a[1])
            if len(pkmn) == 0:
                raise ValueError ("Error por tipo de Pokemon no existente o mal escrito, por favor inténtelo nuevamente.")
            arc.close()    
            return(pkmn)
#print(pykas_tipo("Fuego", "pykadex.csv"))      

#Item B.
def evolucion(pykamon, archivo):
    Flag = True
    while Flag:
        try:
            arc = open(archivo, "r")
        except BaseException as err:
            print("Lo sentimos, su archivo ha sufrido el siguiente error:\n", err)
            print ("\nPor favor, intententelo nuevamente.")
            break
        else:
            Flag = False
            evos = []
            evolve = "Agumon"
            cont = 0
            for line in arc:
                todo = line.strip("\n")
                a = todo.split(",")
                if evolve in a:
                    if "Si" in a:
                        evolve = a[-1]
                        evos.append(evolve)
                if pykamon in a:
                    cont += 1
                    if "Si" in a:
                        if (pykamon!=a[-1]) and (pykamon!=a[-2]) and (pykamon!=a[-3]):
                            evolve = a[-1]
                            evos.append(evolve)
                if pykamon == "Eevolver":
                    evos = ["Auroreon","Volteon","Flameon"]
            if cont == 0:
                raise ValueError ("El Pokémon introducido no existe o está mal escrito, por favor inténtelo nuevamente.")
            if len(evos) == 0:
                print ("Su Pokémon está en última fase evolutiva o no tiene evoluciones.")
            arc.close()
            return(evos)
#print (evolucion("Pykasho", "pykadex.csv"))

#Item C.


            
            
            
            
            
            
            
            
            
