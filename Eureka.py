#12- Teniendo en cuenta que la clave es “eureka”, escribir un algoritmo que nos pida una clave. Solo tenemos 3 intentos
#para acertar, si fallamos los 3 intentos nos mostrará un mensaje indicándonos que hemos agotado esos 3 intentos. Si
#acertamos la clave, saldremos directamente del programa.


print("introducir la clave de cliente")
clave= "eureka"

for i in range(1,4):
    intento=input()
    if intento==clave:
        print("bienvenido")
        break
    else:
        print(f"clave incorrecta intentos {i}/3")