
#   4) Escribí un programa que permita almacenar y consultar números telefónicos.
#   • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#   • Luego, pedí un nombre y mostrale el número asociado, si existe.
print("\n--- Ejercicio N°4 ---")
contactos = {}
for i in range(5):
    # Solicitar al usuario que ingrese el nombre y número del contacto
    nombre = input(f"Ingrese el nombre del contacto {i + 1}: ").title()
    numero = input(f"Ingrese el número del contacto {i + 1}: ")
    # Se almacena el contacto en el diccionario de contactos
    contactos[nombre] = numero
    print("-------------------------------------------------------")
    
    # Validar que el nombre contenga solo letras y el número solo dígitos
    while not nombre.isalpha() or not numero.isdigit():
        print("Error: El nombre debe contener solo letras y el número solo dígitos.")
        nombre = input(f"Ingrese el nombre del contacto {i + 1}: ").title()
        numero = input(f"Ingrese el número del contacto {i + 1}: ")
        print("-------------------------------------------------------")
        contactos[nombre] = numero
        print(contactos)

# Solicitar al usuario que ingrese el nombre del contacto que desea buscar       
buscar_nombre = input("Ingrese el nombre del contacto que desea buscar: ").title()
# Se veridfica si el nombre ingresado se encuentra en el diccionario de contactos y se muestra
if buscar_nombre in contactos:
    print(f"El número de {buscar_nombre} es: {contactos[buscar_nombre]}")
else:
    print(f"El contacto {buscar_nombre} no se encuentra en la lista.")