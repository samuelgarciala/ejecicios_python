
def union_de_2_elementos_conjuntos(set_1,set_2):
    union=set_1.union(set_2)
    #union=set_1|set_2
    return union

def interseccion_de_2_elementos_conjuntos(set_1,set_2):
    interseccion=set_1.intersection(set_2)
    #interseccion=set_1 & set_2
    return interseccion


lista_1=[1,2,3,4,5]
lista_2=[4,5,6,7]

set_1=set(lista_1)
set_2=set(lista_2)

def main():
    interseccion=interseccion_de_2_elementos_conjuntos(set_1,set_2)
    union=union_de_2_elementos_conjuntos(set_1,set_2)
    print(f"interseccion"[interseccion])
    print(f"union"[union])

main()