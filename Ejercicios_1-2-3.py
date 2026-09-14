
#           Actividades
#       Ejercicios 1, 2 y 3
  
# Definición del diccionario base
# se define un diccionario llamado datos_originales que contiene frutas como claves y sus precios como valores.
datos_originales = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Se crea una copia del diccionario datos_originales y se asigna a la variable precios_frutas.
precios_frutas = datos_originales.copy()

# Al crear un Menu de opciones, Utilizando un bucle while, Me encontre con el problema de que el
# diccionario precios_frutas se estaba modificando en cada iteración del bucle, lo que provocaba que 
# los cambios realizados en un ejercicio afectaran a los ejercicios posteriores. Para solucionar esto, se decidió
# restablecer los precios iniciales del diccionario antes de cada ejercicio, utilizando la copia de datos_originales.
while True:
    print("\n--- Menu Ejercicios 1, 2, 3 ---")
    print("1. Se agregan frutas con sus precios")
    print("2. Actualizar precios de frutas")
    print("3. Convertir a lista de frutas sin precios")
    print("4. Restablecer precios iniciales")
    print("5. Salir")

    opcion = int(input("Ingrese la opción deseada: "))

    if opcion == 1:
        # EJERCICIO N°1
        print("\n--- Ejercicio N°1 ---")
        # Se muestra la lista original
        print("Lista Original:")
        print(datos_originales)
        print("-------------------------------")

        # Añadir las siguientes frutas con sus respectivos precios:
        #  ● Naranja = 1200
        #  ● Manzana = 1500
        #  ● Pera = 2300 
        precios_frutas['Naranja'] = 1200
        precios_frutas['Manzana'] = 1500
        precios_frutas['Pera'] = 2300
        # Se imprime por pantalla el diccionario con las claves nuevas y sus
        # valores respectivos
        print("Lista con productos agregados:")
        print(precios_frutas)

    elif opcion == 2:
        # EJERCICIO N°2
        #   2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar 
        #   el código desarrollado en el punto anterior, actualizar los precios de las 
        #   siguientes frutas:
        #   ● Banana = 1330
        #   ● Manzana = 1700
        #   ● Melón = 2800
        
        precios_frutas['Banana'] = 1330
        precios_frutas['Manzana'] = 1700
        precios_frutas['Melón'] = 2800

        print("\n--- Ejercicio N°2 ---")
        # Se imprime por pantalla el diccionario con los precios actualizados
        print("Lista con precios actualizados:")
        print(precios_frutas)

    elif opcion == 3:
        # EJERCICIO N°3
        # 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar 
        # el código desarrollado en el punto anterior, crear una lista que contenga 
        # únicamente las frutas sin los precios.
        print("\n--- Ejercicio N°3 ---")
        
        # Se crea una lista con las claves del diccionario precios_frutas
        lista_frutas = list(precios_frutas.keys())
        
        # Se imprime por pantalla la lista de frutas sin precios
        print("Lista de frutas sin precios:")
        print(lista_frutas)

    elif opcion == 4:
        # Se restablecen los precios iniciales del diccionario
        precios_frutas = datos_originales.copy()
        print("\nSe han restablecido los precios iniciales.")
        
    elif opcion == 5:
        # Salir del programa
        print("\n¡Hasta luego!")
        break
    else:
        # Opción no válida
        print("\nOpción no válida. Intente nuevamente.")