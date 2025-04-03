inventario = {"agua": {"precio": 10, "stock": 2}, "cola": {"precio": 12, "stock": 6}, "naranja": {"precio": 12, "stock": 4}}

def calcular_valor_total_inventario(inventario):
    lista_cantidad_valor_individual=[]
    for dic_producto in inventario.values():
        precio_total=1
        for dic_precio_stock in dic_producto.values():
            precio_total*=dic_precio_stock
        lista_cantidad_valor_individual.append(precio_total)
            
    valor_inventario=sum(lista_cantidad_valor_individual)
    return valor_inventario
        
def main():
    valor_inventario=calcular_valor_total_inventario(inventario)
    print(valor_inventario)

main()