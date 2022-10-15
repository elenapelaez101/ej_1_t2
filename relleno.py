class Punto:
    def __init__(self,x=0,y=0):
        x = self.x
        y = self.y
    
    def __str__(self):
        formato = "({0},{1})".format(self.x,self.y)
        return formato
    def cuadrante(self):
        cuadrante = None
        if self.x > 0 and self.y> 0:
            cuadrante = "Primer cuadrante"
        elif self.x > 0 and self.y< 0:
            cuadrante = "Segundo cuadrante"
        elif self.x < 0 and self.y< 0:
            cuadrante = "Tercer cuadrante"
        elif self.x < 0 and self.y > 0:
            cuadrante = "Cuarto cuadrante"
        elif self.x == 0 and self.y != 0:
            cuadrante = "Sobre el eje y"
        elif self.x != 0 and self.y == 0:
            cuadrante = "Sobre el eje x"
        elif self.x == 0 and self.y == 0:
            cuadrante = "Sobre el origen"
        return cuadrante
    