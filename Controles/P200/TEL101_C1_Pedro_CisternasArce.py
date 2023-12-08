print ("¡Bienvenido a El Master!")
print ("La mejor comida rápida hecha en Pyland.")
a = 0 #Completos Express
b = 0 #Sushi-ca Hamburguesas.
c = 0 #Papas Fritas de Mali.
a_1 = 0 #Ganancia Completos.
b_1 = 0 #Ganancia Hamburguesas.
c_1 = 0 #Ganancia Papas Fritas.
money = 0 #Contador total de dinero recaudado.
while money >= 0:
  print ("")
  print ("El Master 2020: Menú.")
  print ("Opción 1: Completo Express.")
  print ("Opción 2: Sushi-ca Hamburguesa.")
  print ("Opción 3: Papas Fritas de Mali.")
  n = int(input("Por favor, seleccione que opción de producto comprará: "))
  if n == 1:
    a += 1
    a_1 += 1000
    money += 1000
    print (""); print ("Completo Express seleccionado. Debe pagar $ 1000.")
  elif n == 2:
    b += 1
    b_1 += 2000
    money += 2000
    print (""); print ("Sushi-ca Hamburguesa seleccionada. Debe pagar $ 2000.")
  elif n == 3:
    c += 1
    c_1 += 1500
    money += 1500
    print (""); print ("Papas Fritas de Mali seleccionadas. Debe pagar $ 1500.")
  elif n == 999:
    print (""); print ("Opción oculta activada."); print ("Día finalizado."); print ("")
    print ("Se han vendido", a, "Completo Express, con una ganancia de: $", a_1)
    print ("Se han vendido"), (b), ("Sushi-ca Hamburguesa, con una ganancia de: $"), (b_1)
    print ("Se han vendido"), (c), ("Papas Fritas de Mali, con una ganancia de: $"), (c_1)
    print ("La recaudación diaria ha sido de: $"), (money)
    print ("")
    if (a > b) and (a > c):
      print ("El producto con mayor demanda han sido los Completos Express.")
      print ("Gracias por preferir El Master, hasta pronto.")
      break
    if (b > a) and (b > c):
      print ("El producto con mayor demanda han sido las Sushi-ca Hamburguesas.")
      print ("Gracias por preferir El Master, hasta pronto.")
      break
    if (c > a) and (c > b):
      print ("El producto con mayor demanda han sido las Papas Fritas de Mali.")
      print ("Gracias por preferir El Master, hasta pronto.")
      break
    if (a == b) and (a != c):
      print ("Tanto los Completos Express como las Sushi-ca Hamburguesas se han vendido en igual medida.")
      print ("Gracias por preferir El Master, hasta pronto.")
      break
    if (b == c) and (b != a):
      print ("Tanto las Sushi-ca Hamburguesas como las Papas Fritas de Mali se han vendido en igual medida.")
      print ("Gracias por preferir El Master, hasta pronto.")
      break
    if (a == c) and (a != b):
      print ("Tanto los Completos Express como las Papas Fritas de Mali se han vendido en igual medida.")
      print ("Gracias por preferir El Master, hasta pronto.")
      break
    if a == b == c == 0:
      print ("Hoy no se ha vendido nada, puede considerar su local en banca rota.")
      print ("Gracias por preferir El Master, hasta pronto.")
      break
    else:
      print ("Los 3 productos del menú se han vendido en igual medida.")
      print ("Gracias por preferir El Master, hasta pronto.")
      break
  else:
    print ("")
    print ("Opción inválida, por favor inténtelo nuevamente.")