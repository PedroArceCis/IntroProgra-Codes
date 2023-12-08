num = int(input("Ingrese un número entero entre 2 y 1000: "))
a = num % 2; b = num % 3; c = num % 5; d = num % 7
e = bool(num != 2); f = bool(num != 3); g = bool(num != 5)
h = bool(num != 7); i = (e and f and g and h); x = num-1
if num >= 2 and num <= 1000:
  print ("Par") if num % 2 == 0 else ("Impar")
  print ("No Primo") if (a==0 or b==0 or c==0 or d==0) and i else ("Primo")
  print ("Conjunto de divisores:")
  print (num)
  while num:
    if x >= 1:
      while x:
        if num % x != 0:
          x -= 1
        else:
          print(x)
          x -= 1
else:
  print ("Número Incorrecto")
