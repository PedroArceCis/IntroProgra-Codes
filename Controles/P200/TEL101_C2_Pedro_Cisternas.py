pilotos = ["Schumi", "Kimi", "Feña", "Lewis", "Prost", "Ayrton", "Fitto", "Fangio", 
"Nico", "Mika", "Piquet", "Seba", "Nigel", "Jackie", "Jacques"]
import random
def carrera(list):
    copialista_1 = list.copy()
    copialista_2 = list.copy()
    resultado=[]
    for i in copialista_2:
        rand = random.randint(0, len(copialista_1)-1)
        popp = copialista_1.pop(rand)
        resultado.append(popp)
    return resultado
p = carrera(pilotos)
print (p)
def puntos(pilotos, list):
    puntos = []
    copylist = list.copy()
    rango = range(45, 2, -3)
    for i in pilotos:
        a = copylist.index(i)
        score = rango[a]
        puntos.append(score)
    return puntos
x = puntos(pilotos,p)
print (x)
Schumi=0; Kimi=0; Feña=0; Lewis=0; Prost=0; Ayrton=0; Fitto=0; Fangio=0
Nico=0; Mika=0; Piquet=0; Seba=0; Nigel=0; Jackie=0; Jacques=0
corredores = [Schumi, Kimi, Feña, Lewis, Prost, Ayrton, Fitto, Fangio, 
Nico, Mika, Piquet, Seba, Nigel, Jackie, Jacques] #Para sumar puntajes.
corredorescopia = pilotos.copy()
N = int(input("Ingrese el número de carreras de esta temporada : "))
s = range(1,N+1)
for i in s:
    a = carrera(pilotos)
    print ("Carrera", i, "Resultados: ", a)
    z = puntos(pilotos,a)
    pos = 0
    for i in z:
        corredores[pos] += z[pos]
        pos += 1
win = max(corredores)        
xd = corredores.append(win)
print (win)
primero = pilotos[xd]
print ("1° Lugar", primero, "- Puntaje: ", win)
del pilotos[xd]
win = max(corredores)        
xd = corredores.append(win)
print (win)
segundo = pilotos[xd]
print ("2° Lugar", segundo, "- Puntaje: ", win)  
del pilotos[xd]
win = max(corredores)        
xd = corredores.append(win)
print (win)
tercero = pilotos[xd]
print ("3° Lugar", tercero, "- Puntaje: ", win)
