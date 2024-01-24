bisiesto = bool
año = int(input("ingresa un año entre 1900 y 2199 a ver si es bisiesto "))
años_bisiestos= año-1900
if año <= 2199 and año >= 1900: #si el valor es mayor que 2199 y menor que 1900 pasa que el año no es valido
    if año / 4 == año//4: #si la division entre 4 es igual a la division entera entre 4 sigue el programa (puede ser bisiesto)
        if año / 400 == año//400: #si la division entre 400 es igual a la division entera entre 400 sigue el programa (es bisiesto)
            bisiesto = True #si bisiesto es true el año es bisiesto
        elif año % 100 == 0: #si modulo de 100 es igual a 0 el año no es bisiesto (el año es multiplo de 100)
            bisiesto= False #si bisiesto es false el año no es bisiesto
        else:
            bisiesto = True
    else:
        bisiesto= False
    if bisiesto == True:
        print (f"el año {año} es bisiesto")
        if años_bisiestos !=1: #si el año es diferente de 1 solo se divide entre 4 para dar la cantidad de años bisiestos hasta el año ingresado
            if año >= 2100: #si el año es mayor que 2100 solo se divide entre 4 para dar la cantidad de años bisiestos hasta el año ingresado (esto es para no tomar en cuenta el 2100)
                print (f"El numero de años bisiestos entre 1900 y {año} es {int(años_bisiestos/4)-1}")
            else: #si el año es menor que 2100 solo se divide entre 4 para dar la cantidad de años bisiestos hasta el año ingresado
                print (f"El numero de años bisiestos entre 1900 y {año} es {int(años_bisiestos/4)}")
        else:
            print (f"El numero de años bisiestos entre 1900 y {año} es {int(años_bisiestos)}")
    else:
        print (f"el año {año} no es bisiesto")
        if año >= 2100:
            print (f"El numero de años bisiestos entre 1900 y {año} es {int(años_bisiestos/4)-1}")
        else:
            print (f"El numero de años bisiestos entre 1900 y {año} es {int(años_bisiestos/4)}")
else:
    print("Este año no es valido")