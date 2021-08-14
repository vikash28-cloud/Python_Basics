# -------------------resolution of  vector---------------------/
'''class vec2d:
    def __init__(self,i,j) :
        self.icap = i
        self.jcap = j

    def __str__(self) :
        return f"{self.icap}i + {self.jcap}j"

class vec3d(vec2d):
    def __init__(self, i, j,k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

vector2d = vec2d(3,5)
vector3d = vec3d(6,3,1)
print(vector2d)
print(vector3d)'''

# -------------------------/
"""class animals:
    animalType = "wild"
class pets(animals):
    color = "white"
class dogs(pets):
    @staticmethod
    def bark():
        print("bow, bow :;'.,;")

a = animals()
p = pets()
d = dogs()
d.bark()
print(d.color)
print(d.animalType)"""

#------------------------------------------/
'''class employee:
    salary = 1000
    increament = 200

    @property
    def salaryAfterIncreament(self):
        return f"salary after the increament is: {self.salary} + {self.increament}"


    @salaryAfterIncreament.setter
    def salaryAfterIncreament(self,val):
        self.increament = val - self.salary

e = employee()
print(e.salary)
e.salaryAfterIncreament  = 1260
print(e.increament)'''

#--------------------complex no.------------------------/
'''class complex:
    def __init__(self,r,i) :
        self.real = r
        self.imaginary = i

    def __add__(self,c):
        return complex(self.real + c.real, self.imaginary+c.imaginary)

    def __str__(self) :
        return f"{self.real} +  {self.imaginary}i"
        
c1= complex(2,4)
c2 = complex(5,3)
print(c1+c2)'''
