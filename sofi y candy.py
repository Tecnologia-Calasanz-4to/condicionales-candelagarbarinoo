pro1= int(input("Ingrese su primer nota"))
pro2= int(input("Ingrese su segunda nota"))
pro3= int(input("Ingrese su tercer nota"))
 
promedio = ( pro1 + pro2 + pro3 ) / 3

if (pro1 < 1) or (pro1 > 10) or (pro2 < 1) or (pro2 > 10) or (pro3 < 1) or (pro3 > 10):
    print("Error")

elif promedio >= 8 and promedio < 10:
    print("Avanzado")

elif promedio >= 6 and promedio < 8:
    print("Suficiente")

elif promedio >= 1 and promedio < 6:
    print("En proceso")

else:
    print("no error")
