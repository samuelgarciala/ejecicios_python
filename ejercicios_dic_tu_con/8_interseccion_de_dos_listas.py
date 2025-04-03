#8 Un gimnasio registra los nombres de los clientes que asisten cada día. Crea una función que compare la asistencia de dos días y muestre los clientes que asistieron ambos días.

lista_de_asistencia_dia_1=["juan","jose","samuel","daniela","julia"]
lista_de_asistencia_dia_2=["manuela","juan","daniela","pedro"]

def interseccion_de_dos_listas(lista_de_asistencia_dia_1,lista_de_asistencia_dia_2):
    conjunto_dia_1=set(lista_de_asistencia_dia_1)
    conjunto_dia_2=set(lista_de_asistencia_dia_2)
    interseccion= conjunto_dia_1 & conjunto_dia_2
    return list(interseccion)
    
def prueba():
    lista_de_asistencia_dia_1=["juan","jose","samuel","daniela","julia"]
    lista_de_asistencia_dia_2=["manuela","juan","daniela","pedro"]  
    interseccion=interseccion_de_dos_listas(lista_de_asistencia_dia_1,lista_de_asistencia_dia_2)
    print(interseccion)

prueba()
