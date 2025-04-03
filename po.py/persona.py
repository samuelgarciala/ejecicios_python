class Persona:
    def __init__(self,n,e):
        self.nombre = n
        self.edad = e
    
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
    
def principal():
    listado_personas=[]
    cantidad_personas=int(input("escriba la cantidad de personas a ingresar: "))
    for i in range (cantidad_personas):
        nombre=input("escribe el nombre de la persona: ")
        edad = int(input("escriba la edad de la persona: "))
        persona= Persona(nombre,edad)
        listado_personas.append(persona)
        
    for p in listado_personas:
        print(p.saludar())

principal()