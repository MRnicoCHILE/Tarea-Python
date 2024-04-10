"""
Confecciona un programa que solicite al usuario ingresar la temperatura en grados Celsius y la
convierta a grados Fahrenheit. Luego, se debe imprimir el resultado en pantalla.

- Confecciona un programa que solicite al usuario (input)
- ingresar la temperatura en grados Celsius y la convierta a grados Fahrenheit
(buscar cual es la formula para convertir de grados celcius a fahrenheit)
- se debe imprimir el resultado en pantalla (Print)

PD: usando float previo al input (con paréntesis) se genera una conversión

"""

Celsius = float(input("Ingresa la temperatura en grados Celsius: "))

# Con esto se busca cambiar la temperatura a grados Fahrenheit

Fahrenheit = (Celsius * 9/5) + 32

# Ahora, se mostrará el resultado en la pantalla

print(f"{Celsius} grados Celsius son equivalentes a {Fahrenheit} grados Fahrenheit")


