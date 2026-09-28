import os

# Funciones para uso del sistema. Limpiar y pausar la terminal.
def limpiar_pantalla():
    os.system("cls")
    
def pausar():
    os.system("pause")
    
# Funciones de la aplicación.
def multiplicar(a, b):
    resultado = a * b
    return resultado

def sumar(a, b):
    resultado = a + b
    return resultado

def restar(a, b):
    resultado = a - b
    return resultado

def division(a, b):
    resultado = a / b
    return resultado

def pedir_numeros():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    return a, b

limpiar_pantalla()

while True:
    print("-------------------------------------")
    print("|      Seleccione una opción        |")
    print("-------------------------------------")
    print("| 1. Multiplicación                 |")
    print("| 2. División                       |")
    print("| 3. Suma                           |")
    print("| 4. Resta                          |")
    print("| 0. Salir                          |")
    print("-------------------------------------")
    
    opcion = input("Ingrese opción: ")
    limpiar_pantalla()
    
    if opcion == "1":
        print("-------------------------------------")
        print("|          Multiplicación           |")
        print("-------------------------------------")
        a, b = pedir_numeros()
        print(f"El resultado de Multiplicar {a} y {b} es: {multiplicar(a, b)}\n")
        pausar()
        limpiar_pantalla()
        
    elif opcion == "2":
        print("-------------------------------------")
        print("|               Divisón             |")
        print("-------------------------------------")
        #a, b = pedir_numeros()
        #print(f"El resultado de la resta entre {a} y {b} es: {restar(a,b)}\n")
        pausar()
        limpiar_pantalla()

    elif opcion == "3":
        print("-------------------------------------")
        print("|               Suma                |")
        print("-------------------------------------")
        a, b = pedir_numeros()
        print(f"El resultado de la suma entre {a} y {b} es: {sumar(a,b)}\n")
        pausar()
        limpiar_pantalla()

    elif opcion == "4":
        print("-------------------------------------")
        print("|               Resta               |")
        print("-------------------------------------")
        a, b = pedir_numeros()
        print(f"El resultado de la resta entre {a} y {b} es: {restar(a,b)}\n")
        pausar()
        limpiar_pantalla()

    elif opcion == "0":
        print("-------------------------------------")
        print("| ¡Hasta luego!                     |")
        print("-------------------------------------")
        break
    
    else:
        print("Opción inválida. Ingrese una opcíón válida.\n")
        pausar()
        limpiar_pantalla()