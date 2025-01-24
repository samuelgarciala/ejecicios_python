#Escribir un programa que pida el año actual y de nacimiento delusuario. 
#Debe calcular su edad, suponiendo que en el año en curso el usuario ya ha cumplido año
print(f"ingrese año actual")

año_actual=int(input())

print(f"ingrese año de nacimiento")
año=int(input())

edad = año_actual - año

print(f"su edad es:{edad}")
