
#EJERCICIO PRACTICO

#Ejercicio: Sistema de Registro de Estudiantes
#Enunciado

#Una academia desea registrar las calificaciones de varios estudiantes. El programa debe solicitar la cantidad de estudiantes y,
#para cada uno, pedir el nombre y la nota final.

#Al finalizar, el programa debe mostrar:

#La lista de estudiantes con sus notas.
#El promedio general de las notas.
#La cantidad de estudiantes aprobados (nota mayor o igual a 70).
#La cantidad de estudiantes reprobados.
#El estudiante con la nota más alta.
# Sistema de Registro de Estudiantes

estudiantes = []

cantidad = int(input("¿Cuántos estudiantes desea registrar?: "))

for i in range(cantidad):
    print(f"\nEstudiante #{i + 1}")

    nombre = input("Nombre: ")
    nota = float(input("Nota final: "))

    estudiante = {
        "nombre": nombre,
        "nota": nota
    }

    estudiantes.append(estudiante)

# Variables para los cálculos
suma_notas = 0
aprobados = 0
reprobados = 0
mejor_estudiante = estudiantes[0]

for estudiante in estudiantes:
    suma_notas += estudiante["nota"]

    if estudiante["nota"] >= 70:
        aprobados += 1
    else:
        reprobados += 1

    if estudiante["nota"] > mejor_estudiante["nota"]:
        mejor_estudiante = estudiante

promedio = suma_notas / cantidad

print("\n========== RESULTADOS ==========")

for estudiante in estudiantes:
    print(f"{estudiante['nombre']} - Nota: {estudiante['nota']}")

print(f"\nPromedio general: {promedio:.2f}")
print(f"Aprobados: {aprobados}")
print(f"Reprobados: {reprobados}")

print("\nMejor estudiante:")
print(f"{mejor_estudiante['nombre']} con {mejor_estudiante['nota']} puntos")


