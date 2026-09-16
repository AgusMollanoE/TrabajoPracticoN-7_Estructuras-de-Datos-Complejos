


# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#   Permití consultar qué actividad hay en cierto día y hora. 


# Se crea un diccionario con las tuplas de (día, hora) como claves y los eventos como valores
agenda = {
    ('Lunes', '10:00'): 'Turno con VTV',
    ('Martes', '14:00'): 'Turno con Medico',
    ('Miércoles', '09:00'): 'Reunion de Trabajo',
    ('Jueves', '18:00'): 'Clase de Programacion I'
}

print("\n-----EJERCICIO N°9-----")
# Se pide al usuario que ingrese dia y hora que desea consultar
consulta_dia = input("\nIngrese el dia que desea consultar: ").title()
consulta_hora = input("Ingrese la hora que desea Consultar (Ejemplo: hh:mm):  ").strip()

# Se guardan los datos ingresados en la variable busqueda
busqueda = (consulta_dia, consulta_hora)

# Se busca los datos ingresados en el diccionario agenda
if busqueda in agenda:
    print("---------------------------------")
    # Se imprime por pantalla la actuvidad encontrada
    print(f"\nActividad: {agenda[busqueda]}")

else:
    # Se imprime por pantalla que no hay actividades en el dia y hora ingresados
    print(f"\nNo hay actividades en el dia {consulta_dia} las {consulta_hora} hs.")