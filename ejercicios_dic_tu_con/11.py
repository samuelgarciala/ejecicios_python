#11- Crea un diccionario que almacene el stock de una tienda. Luego, implementa una función para actualizar el
#stock cuando se realice una venta.


def actualizar_venta(stock_actual,producto_vendido,cantidad_producto_vendido):
#    stock_actual[producto_vendido]=stock_actual.get(producto_vendido) - cantidad_producto_vendido
    stock_actual[producto_vendido]-=cantidad_producto_vendido

def main():
    stock_actual={
    "agua":40,
    "cola":35,
    "fanta":20,
    "cerveza":30
    }
    actualizar_venta(stock_actual,"agua",10)
    print(stock_actual)
    
main()