#7- Una ciudad mide su temperatura diaria y la almacena en una tupla. Crea una función que devuelva el promedio
#de temperatura.

def temperatura_promedio(datos_almacenados_temperaturas):
    dias_la_muestra=len(datos_almacenados_temperaturas)
    sumas_temperaturas=0
    for temperatura in datos_almacenados_temperaturas:
        sumas_temperaturas+=temperatura
    temperatura_promedio = sumas_temperaturas/dias_la_muestra
    
    return temperatura_promedio
