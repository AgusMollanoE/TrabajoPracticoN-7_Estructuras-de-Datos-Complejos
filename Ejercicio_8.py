
# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#   Permití al usuario:

#  • Consultar el stock de un producto ingresado.
#  • Agregar unidades al stock si el producto ya existe. 
# • Agregar un nuevo producto si no existe. 

# se crea un diccionario con los productos y su stock inicial
productos_stock = {'Martillo': 10, 'Destornillador': 15, 'Taladro': 5, 'Cinta aislante': 8}

print("----Ejercicio N°8----")
# Se muestra el diccionario de productos y su stock inicial
print("Stock Inicial de Productos:")
for producto, stock in productos_stock.items():
    print(f"{producto}: {stock} unidades")
print("-------------------------------")

opcion = ""
while opcion != "5":
    print("Opciones:")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades al stock")
    print("3. Agregar nuevo producto")
    print("4. Consultar stock general de todos los productos")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    
# OPCION | 1: Consultar stock de un producto
    if opcion == "1":
        # Solicitar al usuario que ingrese el nombre del producto a consultar        
        producto = input("Ingrese el Producto a consultar: ").title()
        # Se verifica si el producto ingresado se encuentra en el diccionario de productos_stock y se muestra su stock
        if producto in productos_stock:
            print("--------------------------------------------")
            print(f"El Stock de {producto} es de {productos_stock[producto]} Unidades")
            print("--------------------------------------------")
            
        # Si el producto no se encuentra en el diccionario, se muestra un mensaje indicando que no existe   
        else:
            print(f"\nEl Producto {producto} no existe en sistema")
            
 # OPCION | 2: Agregar unidades al stock de un producto existente           
    elif opcion == "2":
        # Solicitar al usuario que ingrese el nombre del producto al que desea agregar unidades
         producto = input("Ingrese el Producto: ").title()
         
         if producto in productos_stock:
             unidades = int(input(" Ingrese Unidades para Agregar:"))
             # Se actualiza el stock del producto sumando las unidades ingresadas al stock actual
             productos_stock[producto] += unidades
             print("--------------------------------------------")
             print(f"El nuevo Stock de {producto} es {productos_stock[producto]} Unidades")
             print("--------------------------------------------")
         
         else:
            print(f"\nEl Producto {producto} no existe en sistema")
             
 # OPCION | 3: Agregar un nuevo producto al diccionario de productos_stock   
    elif opcion == "3":
        # Solicitar al usuario que ingrese el nombre del nuevo producto a agregar
        producto_nuevo = input("Ingrese un Nuevo Producto: ").title()
        
        # Se verifica si el producto ya existe en el diccionario de productos_stock, si es así, se muestra un mensaje
        # indicando que ya existe y se sugiere usar la opción 2 para sumar stock.
        if producto_nuevo in productos_stock:
            print(f"\nEl Producto {producto_nuevo} ya existe en el Stock. Usa Opcion 2 para sumar Stock ")    
       
        # Si el producto no existe en el diccionario, se solicita al usuario que ingrese las unidades de stock       
        else:    
            unidad_nueva = int(input(f"\nIngrese las unidades de Stock de {producto_nuevo}: "))  
            productos_stock[producto_nuevo] = unidad_nueva
            print("--------------------------------------------")
            # Se muestra un mensaje indicando que el nuevo producto ha sido agregado con éxito y se muestra
            print(f"¡ÉXITO! Producto '{producto_nuevo}' registrado correctamente ({unidad_nueva} unidades).")
            print("--------------------------------------------")
            
# OPCION | 4: Consultar stock general de todos los productos
    elif opcion == "4":
        # Se muestra el stock general de todos los productos en el diccionario productos_stock
        print("--- Stock General de Todos los Productos ---\n")
        for producto, stock in productos_stock.items():
            print(f"{producto}: {stock} unidades")
            print("--------------------------------------------")
            
# OPCION | 5: Salir del programa           
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    
    
    
    