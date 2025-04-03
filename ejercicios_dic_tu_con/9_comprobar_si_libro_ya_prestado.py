#9- Una biblioteca tiene una lista de libros prestados. Si alguien intenta pedir un libro que ya fue prestado, no debe permitirse.

def buscar_si_libro_prestado(disponibilidad_de_libros,libro_a_buscar):
        for libro,disponibilidad in disponibilidad_de_libros.items():
            if libro == libro_a_buscar:
                return disponibilidad

def prueba(): 
    esta=None
    libro_a_buscar= input("introduzca libro a buscar: ")
    disponibilidad_de_libros={
    "harry potter": True,
    "peter pan":True,
    "matematicas 2":True,
    "fisica 4":False,
    "fisica 6":False,
    }
    
    disponibilidad=buscar_si_libro_prestado(disponibilidad_de_libros,libro_a_buscar)
    if disponibilidad == True:
        print(f"esta disponible el libro")
    else:
        print(f"no esta disponible el libro")

prueba()



