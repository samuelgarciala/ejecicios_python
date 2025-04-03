class Coche:
    def __init__(self,marca,modelo,año):
        self.marca_de_coche=marca
        self.modelo_de_coche=modelo
        self.año_de_coche=año
    
    def detalles(self):
        print(f"el coche es {self.marca_de_coche}, modelo es {self.modelo_de_coche} y el año {self.año_de_coche}")
        
coche_1=Coche("Audi","ford",2011)
coche_1.detalles()

        