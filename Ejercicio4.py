#Pide al usuario que ingrese tres calificaciones (por ejemplo, de 0 a 10) y calcula el promedio de esas calificaciones. Muestra el resultado.

nota1 = float(input("Ingrese la primer nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercer nota: "))

promedio = (nota1 + nota2 + nota3) / 3

print(f"El promedio es: {promedio}")
