#%%
from matplotlib import pyplot as plt

class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    # Used with `repr()`
    def __repr__(self):
        return f'Punto({self.x}, {self.y})'

    def __add__(self, b):
        return Punto(self.x + b.x, self.y + b.y)
    
class Rectangulo():
    def __init__(self, punto1, punto2):
        """
        recibe 2 puntos como parámetros y genera
        un rectángulo o en un caso particular de él
        un cuadrado
        """
        self.vertice1 = (punto1.x, punto1.y)
        self.vertice2 = (punto1.x, punto2.y)
        self.vertice3 = (punto2.x, punto2.y)
        self.vertice4 = (punto2.x, punto1.y)
        self.punto1 = punto1
        self.punto2 = punto2

    def base(self):
        """
        calcula la base
        """
        return abs(self.vertice1[0] - self.vertice3[0])
    
    def altura(self):
        """
        calcula la altura
        """
        return abs(self.vertice1[1] - self.vertice2[1])

    def area(self):
        """
        calcula el área
        """
        return self.base * self.altura
    
    def __str__(self):
        """
        Devuelve los puntos que forman el rectángulo
        """
        return "(" + str(self.vertice1) + ", "  + str(self.vertice2) + ", " + str(self.vertice3) + ", " + str(self.vertice4) + ")"

    def __repr__(self):
        return f'Rectangulo({self.vertice1}, {self.vertice2}, {self.vertice3}, {self.vertice4})'

    def desplazar(self,desplazamiento):
        """
        desplaza los vertices a partir de un punto que se le suma
        con coordenada x,y y de clase "Punto"
        """
        self.punto1 =  self.punto1 + desplazamiento
        self.punto2 =  self.punto2 + desplazamiento
        self.vertice1 = (punto1.x, punto1.y)
        self.vertice2 = (punto1.x, punto2.y)
        self.vertice3 = (punto2.x, punto2.y)
        self.vertice4 = (punto2.x, punto1.y)
    
    def vertices(self):
        return [self.vertice1, self.vertice2, self.vertice3, self.vertice4]

    def vertice_inferior_derecho(self):
        vertices = self.vertices()
        ver_inf_der = vertices.pop(0) 
        for vertice in vertices:
            ver_inf_der = vertice if ((vertice[0] >= ver_inf_der[0]) and (vertice[1] <= ver_inf_der[1])) else ver_inf_der
        return ver_inf_der

    def rotar(self):
        punto1 = Punto(self.vertice_inferior_derecho()[0], self.vertice_inferior_derecho()[1])
        punto2 = Punto(punto1.x + self.altura(), punto1.y + self.base())
        self.vertice1 = (punto1.x, punto1.y)
        self.vertice2 = (punto1.x, punto2.y)
        self.vertice3 = (punto2.x, punto2.y)
        self.vertice4 = (punto2.x, punto1.y)
#%%
rectangulo = Rectangulo(Punto(0,0),Punto(10,5))
plt.scatter([rectangulo.vertice1[0],rectangulo.vertice2[0],rectangulo.vertice3[0],rectangulo.vertice4[0]],[rectangulo.vertice1[1],rectangulo.vertice2[1],rectangulo.vertice3[1],rectangulo.vertice4[1]])

#%%
rectangulo.rotar()
rectangulo.vertices()
#%%
plt.scatter([rectangulo.vertice1[0],rectangulo.vertice2[0],rectangulo.vertice3[0],rectangulo.vertice4[0]],[rectangulo.vertice1[1],rectangulo.vertice2[1],rectangulo.vertice3[1],rectangulo.vertice4[1]])
#%%
rectangulo
#%%
str(rectangulo)

#%%
punto1 = Punto(1,2)
punto2 = Punto(2,2)
punto3 = (punto1 + punto2)

#%%
rectangulo.vertice_inferior_derecho()

#%%
ul = Punto(0,2)
lr = Punto(1,0)
ll = Punto(0,0)
ur = Punto(1,2)
rect1 = Rectangulo(ul,lr)
rect2 = Rectangulo(ll,ur)
#%%
rect2.altura()