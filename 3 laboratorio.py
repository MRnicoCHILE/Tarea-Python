"""
Supón que un ramo tiene las siguientes evaluaciones:
• 3 tareas en Laboratorio, estas valen un 15% del curso,
• 3 tareas en clase, que valen un 15% del curso,
- 2 notas solemnes cada una un 35%

Elabora un programa que, ingresando todas las notas, entregue la nota de presentación.
Ejemplo:
Lab 1 = 4.5
Lab 2 = 7.0
Lab 3 = 5.5
Tarea 1 = 6.2
Tarea 2 = 5.0
Tarea 3 = 2.1
Solemne 1 = 1.8
Solemne 2 = 5.4

Nota de presentación = (Prom Lab)*0,15 + (Prom Tareas)*0.15 + Sol1*0.35 + Sol2*0.35
Prom Lab = 5.7
Prom Tarea = 4.4
Nota de presentación = 5.7*0.15 + 4.4*0.15 + 1.8*0.35 + 5.4*0.35
Nota de presentación = 4.0
"""

#Definir variables y los tipos de datos

lab1 = float(input("Ingresa la nota de laboratorio 1: "))
lab2 = float(input("Ingresa la nota de laboratorio 2: "))
lab3 = float(input("Ingresa la nota de laboratorio 3: "))

#Ahora se definen las 3 notas de las tareas

tarea1 = float(input("Ingresa la nota de la tarea 1: "))
tarea2 = float(input("Ingresa la nota de la tarea 2: "))
tarea3 = float(input("Ingresa la nota de la tarea 3: "))

#Ahora se solicitan las notas de los solemnes

solemne1 = float(input("Ingresa la nota de solemne 1: "))
solemne2 = float(input("Ingresa la nota de solemne 2: "))

#Se calcula el promedio 

prom_lab = (lab1 + lab2 + lab3) / 3
prom_tareas = (tarea1 + tarea2 + tarea3) / 3

#Se calcula la nota de presentación

nota_presentacion = (prom_lab * 0.15) + (prom_tareas * 0.15) + (solemne1 * 0.35) + (solemne2 * 0.35)

#Se imprime el resultado

print(f"Este es el promedio de los laboratorios = {prom_lab}\n")
print(f"Este es el promedio de las tareas = {prom_tareas}\n")
print(f"La nota de presentación es = {nota_presentacion}\n")