#5- Encontrar el elemento más repetido en una tupla.
#solo funciona para un solo elemento

def contar_caracteres_en_tupla(tupla):
    diccionario={}
    for caracter in tupla:
        if caracter not in diccionario:
            diccionario[caracter]=1
        else:
            diccionario[caracter]+=1
    return diccionario


def elemento_mayor_de_diccionario(diccionario):  
    elemento_mayor=None
    valor_mayor=0
    for key,valor in diccionario.items():
        
        if valor > valor_mayor:
            valor_mayor=valor
            elemento_mayor=key
            
    return elemento_mayor

def main():
    tupla = (1,2,3,4,5,6,6,7)
    diccionario_de_tupla=contar_caracteres_en_tupla(tupla)
    elemento_mayor=elemento_mayor_de_diccionario(diccionario_de_tupla)
    print(elemento_mayor)
    
main()

     
    