#14- Crea un diccionario que almacene productos con su precio y stock. Luego, crea una función para calcular el
#valor total del inventario.

#modificar agregar el stock

#def introducir_datos():
#    inventario={}
#    clave=None
#    while True:
#        producto=input("introducir el producto: ")
#        inventario[producto]=int(input("introduccir precio: "))
#        clave=input("introduzca la letra x si quiere terminar con el registro")
#        if clave == "x":
#            break
#        
#    return inventario

inventario = {"agua": {"precio": 10, "stock": 2}, "cola": {"precio": 12, "stock": 6}, "naranja": {"precio": 12, "stock": 4}}

def calcular_valor_total_inventario(inventario):
    lista_cantidad_valor_individual=[]
    for dic_producto in inventario.values():
        precio=dic_producto["precio"]
        stock=dic_producto["stock"]
        precio_total=precio*stock
        lista_cantidad_valor_individual.append(precio_total)
            
    valor_inventario=sum(lista_cantidad_valor_individual)
    return valor_inventario
        
def main():
    valor_inventario=calcular_valor_total_inventario(inventario)
    print(valor_inventario)

main()