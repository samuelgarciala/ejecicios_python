class Persona:
    def __init__(self,nombre,edad,ciudad):
        self.nombre_persona=nombre
        self.edad_persona=edad
        self.ciudad_persona=ciudad
        
    def presentarse(self):
        print(f"Hola, soy {self.nombre_persona}, tengo {self.edad_persona} y vivo en la {self.ciudad_persona}")

persona_1=Persona("jose",21,"madrid")
persona_1.presentarse()


