import math

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
        vector = "("+str(self.x2 - self.x)+","+str(self.y2-self.y)+")"
        return vector
    def distancia(self,x3=0, y3=0):
        self.x3 = x3
        self.y3= y3
        vecti = self.x3-self.x, self.y3- self.y
        distancia= round(math.sqrt(vecti[0]**2+vecti[1]^2),2)
        return distancia


class Rectangulo:
    def __init__ (self, xpi=0, ypi=0, xpf=0, ypf=0):
        self.xpi = xpi
        self.ypi = ypi
        self.xpf = xpf
        self.ypf = ypf
    def base(self):
        base = abs(self.xpf - self.xpi)
        print("La base del rectángulo mide "+str(base)+" unidades")
    
    def altura(self):
        altura = abs(self.ypf - self.ypi)
        print("La altura del rectángulo mide "+str(altura)+" unidades")

    def area(self):
        area = abs((self.xpf - self.xpi) * (self.ypf - self.ypi))
        print("El area del rectángulo mide "+str(area)+" unidades cuadradas")

miprimpunto = Punto(1,2)
print(miprimpunto.cuadrante())
print(miprimpunto.vector(4,7))
miprimpunto.distancia(2,5)

recti = Rectangulo(1,4,8,-3)
recti.base()
recti.altura()
recti.area()
#Pruebas
#Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla
A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3,-1)
D = Punto(0,0)

print(A)
print(B)
print(C)
print(D)

#Consulta a que cuadrante pertenecen el punto A, C y D.
print("\nA se encuentra en el "+A.cuadrante())
print("B se encuentra en el "+C.cuadrante())
print("D se encuentra en el "+D.cuadrante())

#Consulta los vectores AB y BA.
print("\nel vector AB es:")
print(A.vector(B.x,B.y))

print("el vector BA es:")
print(B.vector(A.x,A.y))

#(Optativo) Consulta la distancia entre los puntos 'A y B' y 'B y A'.
print("\nDistancia entre los puntos A y B: "+str(A.distancia(B.x, B.y))+ " unidades")

print("\nDistancia entre los puntos B y A: "+str(B.distancia(A.x, A.y))+ " unidades")


#(Optativo) Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0).
print("\n")
a = A.distancia(D.x, D.y)
b = B.distancia(D.x, D.y)
c = C.distancia(D.x, D.y)
print (a)

print
#Crea un rectángulo utilizando los puntos A y B
r = Rectangulo(A.x,A.y,B.x,B.y)
#Consulta la base, altura y área del rectángulo.
r.base()





