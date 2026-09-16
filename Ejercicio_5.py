
# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra. 

# Solicitar al usuario que ingrese una frase
frase = input("Ingrese un Frase: ")

# Se divide la frase en palabras utilizando el método split() y se almacena en una lista
palabras = frase.split()

# Se crea un conjunto (set) para obtener las palabras únicas de la lista de palabras
palabras_unicas = set(palabras)

# Se crea un diccionario para contar la cantidad de veces que aparece cada palabra en la lista de palabras
recuento_dic = {}

# Se recorre la lista de palabras y se actualiza el diccionario con el recuento de cada palabra
for palabra in palabras:
    # Se verifica si la palabra ya está en el diccionario, si es así, se incrementa su contador en 1, 
    # de lo contrario, se agrega al diccionario con un contador inicial de 1
    if palabra in recuento_dic:
        recuento_dic[palabra] += 1
    else:
        recuento_dic[palabra] = 1
        
# Se imprime por pantalla el conjunto de palabras únicas y el diccionario con el recuento de palabras
print("Palabras únicas:", palabras_unicas)
print("Recuento de palabras:", recuento_dic)

