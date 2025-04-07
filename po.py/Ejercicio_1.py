class Circulo:
    def __init__(self,radio):#constructor
        self.radio_del_circulo=radio
    
    def calcular_area(self):
        area=self.radio_del_circulo**2 * 3.14
        return area
    
    def calcular_perimetro(self):
        perimetro=self.radio_del_circulo*2*3.14
        return perimetro

class Cuadrado:
    def __init__(self,lado):
        self.lado_del_cuadrado=lado
    
    def calcular_area(self):
        area=self.lado_del_cuadrado**2
        return area
    
    def calcular_perimetro(self):
        perimetro=self.lado_del_cuadrado*4
        return perimetro
    
circulo_1= Circulo(5)
area=circulo_1.calcular_area()
perimetro=circulo_1.calcular_perimetro()

print(f"el area del circulo es: {area}, el perimetro es: {perimetro}")

cuadrado_1= Cuadrado(4)
area=cuadrado_1.calcular_area()
perimetro=cuadrado_1.calcular_perimetro()

print(f"el area del cuadrado es: {area}, el perimetro es: {perimetro}")

