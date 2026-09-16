
#   6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego,
#   mostrá el promedio de cada alumno. 

alumnos = {}

for i in range(3):
    # Solicitar al usuario que ingrese el nombre del alumno
    nombre = input(f"Ingrese el Nombre del alumno {i + 1}: ").title()
    
    # Solicitar al usuario que ingrese las 3 notas del alumno y almacenarlas en una tupla
    nota1 = float(input(f"Ingrese la nota 1 del alumno {nombre}: "))
    nota2 = float(input(f"Ingrese la nota 2 del alumno {nombre}: "))
    nota3 = float(input(f"Ingrese la nota 3 del alumno {nombre}: "))
    print("-------------------------------------------------------")
    
    # Se almacena el nombre del alumno como clave y la tupla de notas como valor en el diccionario alumnos
    alumnos[nombre] = (nota1, nota2, nota3)
    print(alumnos)
    
print("-----Resultados-----")
    # Se recorre el diccionario de alumnos y se calcula el promedio de cada alumno
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
         
    # Se imprime por pantalla el promedio del alumno con dos decimales    
    print(f"el promedio del alumno {nombre} es : {promedio:.2f} ")
    
    