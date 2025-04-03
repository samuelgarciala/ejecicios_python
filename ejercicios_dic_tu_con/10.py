#10- Un instituto registra por cada estudiante su nombre y las notas de 5 asignaturas.
# Se necesita devolver los estudiantes cuyo promedio de notas no supera un valor dado.


notas_de_estudiantes={
    
    "estudiante_1":{"matematicas":7,"fisica":9,"quimica":4,"castellano":7,"sociales":3},
    "estudiante_2":{"matematicas":10,"fisica":10,"quimica":9,"castellano":9,"sociales":8},
    "estudiante_3":{"matematicas":3,"fisica":4,"quimica":5,"castellano":8,"sociales":4},
}

def estudiante_aprobados_reprobados(notas_de_estudiantes,nota_minima):
    lista_de_aprobados=[]
    lista_de_reprobados=[]
    
    for estudiante,valor_materia_nota in notas_de_estudiantes.items():
        promedio= sum(valor_materia_nota.values())/len(valor_materia_nota.keys())

        if promedio >= nota_minima:
            lista_de_aprobados.append(estudiante)
        else:
            lista_de_reprobados.append(estudiante)
    
    print(f"aprobados: {lista_de_aprobados}")
    print(f"reprobados: {lista_de_reprobados}")
    
def main():
    nota_minima=int(input("introduzca nota minima: "))
    estudiante_aprobados_reprobados(notas_de_estudiantes,nota_minima)
    
main()
                
            