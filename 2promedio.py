"""
Realiza un programa que reciba tres números por teclado y calcule su promedio, se debe mostrar el
resultado en pantalla.

- El programa debe recibir tres números por teclado
- El programa debe calcular el promedio de los 3 números
- Luego debe mostrar el resultado en pantalla
"""
# Iniciar variables para almacenar números ingresados por el usuario

numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
numero3 = float(input("Ingrese el tercer número: "))

# Ahora se calculará el promedio de los 3 números

promedio = (numero1 + numero2 + numero3) / 3

# Mostrar resultado en la pantalla con un número redondeado

input(f"El promedio de la suma de las notas es: {round(promedio)}")