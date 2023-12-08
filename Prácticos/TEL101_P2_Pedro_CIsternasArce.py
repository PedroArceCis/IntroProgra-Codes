print ("¡Bienvenido a PasoPalabra!")
print ("")
print ("Éste es su detector de palabras palíndromas.")
print ("")
print ("Por favor, recuerde introducir una palabra en minúsculas para que el sistema funcione correctamente.")
print ("")
#Tengo fé de que se reconozcan las referencias en los modos ;;
palabra = str(input("Ingrese su palabra: "))
print ("")
if palabra[0:] == palabra[::-1]:
  print ("Easy mode: SUCCESS!")
else:
  print ("Easy mode: FAILURE")
a = list(palabra)
b = list(palabra)
b.reverse()
if a == b:
  print ("Normal mode: SUCCESS!")
else:
  print ("Normal mode: FAILURE")
while len(a)>1 and (a[0])==(a[-1]):
  del a[0]
  del a[-1]
if len(a) <= 1:
  print ("Hard mode: SUCCESS!")
  print ("")
  print ("WOOW! INCREDIBLE!!")
  print ("")
  print ("Su palabra es palíndroma.")
else:
  print ("Hard mode: FAILURE")
  print ("")
  print ("GAME OVER")
  print ("")
  print ("Su palabra no es palíndrma.")