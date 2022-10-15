class Punto:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        print("Se ha generado tu punto")
    
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
    def vector(self,x2=0,y2=0):
        self.x2= x2
        self.y2 =y2
        vector = "("+self.x2 - self.x+","+self.y2-self.y+")"
        return vector

miprimpunto = Punto(1,2)
print(miprimpunto.cuadrante())



