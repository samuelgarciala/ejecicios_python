#13- Dado un diccionario con equipos y jugadores, muestra qué jugadores están inscritos en varios equipos.
 #invertir usar equipo clave
 
diccionario_equipos={
    "chelsea":["juan","peter","harry","pedro"],
    "real madrid":["peter","harry","daniel"],
    "barcelona":["juan","pedro","jose"],
    }
#diccionario_equipos={
#    "harry": ["chelsea"],
#    "peter":["real madrid"],
#    "daniel":["barcelona","las  palmas"],
#    "juan":["las  palmas"],
#    "jose":["real madrid","barcelona"],
#    }

lista_de_jugadores=[]

for equipo,jugador in diccionario_equipos.items():
    
    copia_diccionario= diccionario_equipos.copy()
    del copia_diccionario[equipo]
    
    if jugador in copia_diccionario.values():
        lista_de_jugadores.append(jugador)

print(lista_de_jugadores)