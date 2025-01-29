#8- Un colegio desea saber qué porcentaje de niños y qué porcentaje de niñas hay en el curso actual. Diseñar un algoritmo
#para este propósito.

print("Introduzca numero total de niños")
total_niños= int(input())
print("Introduzca numero total de niños")
total_niñas= int(input())

porcentaje_de_niños = total_niños/(total_niñas+total_niños) *100
porcentaje_de_niñas = 100-porcentaje_de_niños

print(f"porcentaje de niños es igual a {porcentaje_de_niños} %")
print(f"porcentaje de niñas es igual a {porcentaje_de_niñas} %")



