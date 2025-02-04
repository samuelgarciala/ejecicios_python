#9- Algoritmo que nos diga si una persona puede acceder a cursar un ciclo formativo de grado superior o no. Para acceder
#a un grado superior, si se tiene un título de bachiller, en caso de no tenerlo, se puede acceder si hemos superado una
#prueba de acceso.

def pedir_titulo_bachiller():
    intentos=0
    entrada_titulo_correcta=False

    while intentos<3 and entrada_titulo_correcta==False:
        intentos=intentos+1
        print("Tiene un titulo de bachiller, si o no?")
        tiene_titulo_bachiller= input()
        if tiene_titulo_bachiller=="si":
            print("puede recibir el ciclo formativo")
            raise SystemExit
        elif tiene_titulo_bachiller=="no":
            entrada_titulo_correcta=True
            
        else:
            entrada_titulo_correcta=False
            print("ha introducido un valor incorrecto")
            if intentos==3:
                print("cerrando programa")
                raise SystemExit

def comprobar_prueba_acceso():
    intentos=0
    while intentos<3:
        intentos=intentos+1
        
        print("ha aprovado la prueba de acceso si o no?")
        prueba_de_acceso= input()
        
        if prueba_de_acceso == "si":
            print("puede recibir el ciclo formativo")
            break
        
        elif prueba_de_acceso == "no":
            print("no puede recibir el ciclo formativo")
            break
        
        else:
            
                print("ha introducido un valor incorrecto")

def mensaje_cerrando_el_programa():
    print("cerrando el programa")

def main():
    pedir_titulo_bachiller()
    comprobar_prueba_acceso()
    mensaje_cerrando_el_programa()

main()