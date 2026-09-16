


# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
#     diccionario donde:
#     • Las capitales sean las claves.
#     • Los países sean los valores. 

paises_capitales = {"Argentina": "Buenos aires", "Venezuela": "Caracas", "Peru": "Lima", "Grecia": "Atenas"}

# Se crea un diccionario vacio, donde se guardaran las claves y valores invertidos de paises_capitales
invertido = {}
print("\n---------- Ejercicio N°10 ----------")
print("\n| Original |")
print("------ Paises y sus capitales ------")
print(paises_capitales)

print("\n| Invertido |")
print("------ Capitales y sus Paises ------")
# Recorre el diccionario usando .items() para obtener clave (pais) y valor (capital) en cada vuelta
for pais, capital in paises_capitales.items():
    # Asigna la capital como nueva clave y el país como su valor
    invertido[capital] = pais
    
# Muestra el nuevo diccionario con las claves y valores invertidos
print(invertido)