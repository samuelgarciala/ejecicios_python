#12- Crea una función que reciba una lista de compras y devuelva la cantidad de veces que se compró cada producto.

def cantidad_veces_que_se_compro(lista_de_compra):
    cantidad_veces_producto={}
    for producto in lista_de_compra:
        if producto not in cantidad_veces_producto:
            cantidad_veces_producto[producto]=1
        else:
            cantidad_veces_producto[producto]+=1
    return cantidad_veces_producto


def main():
    lista_de_compra=["agua","leche","tomate","leche","agua","agua"]
    cantidad_veces_producto=cantidad_veces_que_se_compro(lista_de_compra)
    for producto,cantidad in cantidad_veces_producto.items():
        print(f"el producto {producto} se ha vendido {cantidad} veces")

main()
    
