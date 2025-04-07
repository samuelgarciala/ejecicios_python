class Rectangulo:
    def __init__(self,ancho,alto):
        self.ancho_rectangulo=ancho
        self.alto_rectangulo=alto
        
    def calcular_area_ractangulo(self):
        return self.ancho_rectangulo * self.alto_rectangulo

rectangulo_1 = Rectangulo(2,2)

print(f"el area del rectangulo es: {rectangulo_1.calcular_area_ractangulo()}")
