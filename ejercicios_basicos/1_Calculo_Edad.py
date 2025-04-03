#Escribir un programa que pida el año actual y de nacimiento del usuario. 
#Debe calcular su edad, suponiendo que en el año en curso el usuario ya ha cumplido año

def entrada_de_datos_año_actual():
    print(f"ingrese año actual")
    año_actual=int(input())
    return año_actual
    
def entrada_de_datos_año_nacimiento():
    print(f"ingrese año de nacimiento")
    año_nacimiento=int(input())
    return año_nacimiento

def calculo_de_edad(año_actual,año_nacimiento):
    edad = año_actual - año_nacimiento
    return edad

def salida_de_datos(edad):
    print(f"su edad es:{edad}")

def main():
    año_actual=entrada_de_datos_año_actual()
    año_nacimiento=entrada_de_datos_año_nacimiento()
    edad=calculo_de_edad(año_actual,año_nacimiento)
    salida_de_datos(edad)
    
main()

