
#7) Se recibe el registro diario de asistencia a una capacitación en forma de lista.
# En dicha lista pueden aparecer nombres repetidos, ya que una misma persona pudo haber
# asistido en más de una jornada.

# • Mostrá la lista original de asistencias.
# • Generá un conjunto (set) a partir de la lista y mostrar los empleados que asistieron al
#   menos una vez (sin repetir nombres).
# • Indicá cuántas veces asistió cada empleado a la capacitación.

asistencia = ['ana', 'misael', 'agustin', 'ana', 'maria', 'juan', 'pedro', 'ana', 'maria', 'juan']

print("----Ejercicio N°7----")
print("\nLista original de asistencias:")
# Se imprime por pantalla la lista original de asistencias
print(asistencia)
print("------------------------------------")

print("Lista de Empleados sin Repetir")
# Se crea un conjunto (set) a partir de la lista de asistencias para obtener los nombres únicos de los empleados
conjunto = set(asistencia)
print(conjunto)
print("------------------------------------")

print("Lista de Asistencias por Empleado")
# Se recorre el conjunto de empleados y se cuenta cuántas veces aparece cada empleado en la lista de asistencias
for empleado in conjunto:
    # Se utiliza el método count() para contar cuántas veces aparece el nombre del empleado en la lista de asistencias
    cantidad = asistencia.count(empleado)
    
    # Se imprime por pantalla el nombre del empleado y la cantidad de veces que asistió a la capacitación
    print(f"El/La empleado(a) {empleado} asistió {cantidad} veces.")
    
    