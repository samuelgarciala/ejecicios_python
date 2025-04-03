#3- Diseñar una aplicación que calcule la longitud y el área de una circunferencia.
def calcular_area_circunferencia(radio):
    area= 3.14 * radio ** 2
    return area

def calcular_longitud_circuferencia(radio):
    logitud= 2 * 3.14 * radio
    return logitud

def entrada_de_datos():
        print("ingrese radio:")
        radio=int(input())
        return radio

def salida_de_datos(area,longitud):
    print(f"el area es {area} y la logitud es {longitud}")

def main():
    r = entrada_de_datos()
    area = calcular_area_circunferencia(r)
    longitud =calcular_longitud_circuferencia(r)
    salida_de_datos(area,longitud)

main()




