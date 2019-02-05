import math
inf = math.inf
class Vector():
    def __init__(self, dimension = 0, liste = ""):
        self.dimension = dimension
        self.liste = liste

        if self.dimension < 0 or not type(self.dimension) is int:
            raise ValueError("Dimension length is invalid or it has invalid type")
        if self.dimension != len(self.liste):
            raise ValueError("Dimension value and vector lenghts are not equal")

    def dot(self, vector):
        self.vector = vector

        if len(self.vector) != len(self.liste):
            return False

        else:
            sonuc = []
            toplam = 0
            for i in range(0,len(self.liste)):
                sonuc.append(self.liste[i]*self.vector[i])
                toplam += sonuc[i]
            print(toplam)

    def __mul__(self, scalar):

        sonuc_scalar = []
        if type(scalar) is int or type(scalar) is float:
            for i in range(0,len(self.liste)):
                sonuc_scalar.append(self.liste[i] * scalar)
            print(sonuc_scalar)
        else:
            for i in range(0,len(self.liste)):
                sonuc_scalar.append(self.liste[i] * scalar.liste[i])
            print(sonuc_scalar)


    def __rmul__(self, scalar):
        sonuc_scalar = []
        for i in range(0, len(self.liste)):
            sonuc_scalar.append(self.liste[i] * scalar)
        print(sonuc_scalar)

    def norm(self,p):


        if p == 0:
            counter = 0
            for i in range(0,len(self.liste)):
                if self.liste[i] != 0:
                    counter += 1

            print(counter)

        if (0 < p) and (p < inf):
            toplam = 0
            sonuc = 0
            for i in range(0,len(self.liste)):
                toplam += (abs(self.liste[i]) ** p)
                sonuc = (toplam ** (1/p))

            print(sonuc)
        if p == inf:
            bos = []
            for i in range(0,len(self.liste)):
                bos.append(abs(self.liste[i]))

            print(max(bos))


vect1 = Vector(3, (1, 2, 0))
vect2 = Vector(3, (1, 2, 3))
#vect3 = Vector(3, (1, -3, 2))
#vect1.norm(0)
#vect2.norm(3)
#vect3.norm(inf)

vect1 * vect2

#vect * 2
#2 * vect
#vect.dot((1, 2, 4))
