#8- Un colegio desea saber qué porcentaje de niños y qué porcentaje de niñas hay en el curso actual. Diseñar un algoritmo
#para este propósito.
def mensaje_inicio(mensaje):
    print(mensaje)

def ingreso_total_de_niños_niñas():
    total_estudiantes= int(input())
    return total_estudiantes

def definir_porcentaje_niños(total_niños,total_alumnos):
    porcentaje_de_niños = total_niños/total_alumnos *100
    return porcentaje_de_niños
    
def definir_porcentaje_niñas(porcentaje_de_niños):
    porcentaje_de_niñas = 100-porcentaje_de_niños
    return porcentaje_de_niñas

def mensaje_final(porcentaje_de_niños,porcentaje_de_niñas):
    print(f"porcentaje de niños es igual a {porcentaje_de_niños} %")
    print(f"porcentaje de niñas es igual a {porcentaje_de_niñas} %")

def main():
    mensaje_inicio("introduzca el total de niños")
    total_niños=ingreso_total_de_niños_niñas()
    mensaje_inicio("introduzca el total de niñas")
    total_niñas=ingreso_total_de_niños_niñas()   
    total_alumnos= total_niñas+total_niños
    porcentaje_niños=definir_porcentaje_niños(total_niños,total_alumnos)
    porcentaje_niñas=definir_porcentaje_niñas(porcentaje_niños)
    
    mensaje_final(porcentaje_niños,porcentaje_niñas)

main()
    