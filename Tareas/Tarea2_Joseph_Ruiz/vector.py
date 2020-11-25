
# coding: utf-8

# # Creando clases
# 
# En el siguiente código se encuentra la construcción de una clase $Vector$ tanto en coordenadas $Cartesianas$ como $Esféricas$ con algunas operaciones fundamentales definidas en su respectivo $Espacio$ $vectorial$ en sus bases estándar.
# 
# ## Introducción: ecuaciones de transformación entre $R^3$ y $V_{r \theta \phi}$
# 
#    Recordemos que las expresiones que relacionan cada componente estan dadas por:
#    
#    $$x = r\ \cos(\phi)\ \sin(\theta)$$
#    $$y = r\ \sin(\phi)\ \sin(\theta)$$
#    $$z = r\ \cos(\theta)$$
#    
#    Equivalentemente,
#    
#    $$r=\sqrt{x^2 +y^2+z^2}$$
#    $$\cos(\theta) = \frac{z}{r}$$
#    $$  \tan{\phi} = \frac{y}{x} $$
#    
#    
# NOTA: El producto interno y vectorial de dos vectores en una base ortonormal dada se define como:
# 
# $$e_i \cdot e_j = \delta_{ij} $$
# 
# $$ e_i\times e_j =\sum \epsilon_{ijk}e_k $$
# 
# 
# 

# In[36]:


import numpy as np
class VectorCartesiano(object):

    '''Es una clase vector en la base cartesiana'''
    def __init__(self, x0=0,y0=0,z0=0):
        self.x = float(x0)
        self.y = float(y0)
        self.z = float(z0)        
        self.magnitud = (self.x**2+self.y**2+self.z**2)**0.5 

    
    def __getitem__(self, key):
        self.values = (self.x,self.y,self.z)
        return self.values[key]
        
    def __add__(self,other):
        '''Sobrecarga del operador suma'''
        return VectorCartesiano(self.x + other.x, self.y + other.y, self.z + other.z)
           
    def __sub__(self,other):        
        '''Sobrecarga del operador resta'''
        return VectorCartesiano(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __eq__(self,other):
        '''Sobrecarga el operador igualdad'''
        
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False
    def __ne__(self,other):
        '''Sobrecarga el operador diferente'''
        
        if self.x != other.x and self.y != other.y and self.z != other.z:
            return True
        else:
            return False
        
    def inner(self, other):
        """ """
        return sum(a * b for a, b in zip(self, other))
    
    def __mul__(self, other):
        """ Regresa el producto punto de vector por otro, si es otro es un vector.
        Si otro es un escalar multiplica cada componente"""
        if type(other) == type(self):
            return self.inner(other)
        elif type(other) == type(1) or type(other) == type(1.0):
            product = tuple( a * other for a in self )
            return VectorCartesiano(*product)
    
    def Cruz(self,other):
        return VectorCartesiano(self.y*other.z-self.z*other.y, self.z*other.x-self.x*other.z, self.x*other.y-self.y*other.x)
    
    def Print(self):
        '''Imprime el vector'''
        print('[ %.1f, %.1f , %.1f]'%(self.x, self.y, self.z))


# In[ ]:





# In[47]:


import math
class VectorPolar(VectorCartesiano):
     
    '''Es una clase Vector en coordenadas esféricas que hereda
    los atributos de VectorCartesiano. Las componentes angulares están
    medidas en radianes'''
    
    def __init__(self,a1=0,a2=0,a3=0, system='cartesian'):
        '''Por defecto el constructor de VectorPolar tomará vectores en el
        sistema Cartesiano, a menos que se especifique system = 'polar' '''
        
        super().__init__(a1,a2,a3)
        vector = (float(a1),float(a2),float(a3))
        
        if system == 'cartesian':
            self.cartesian = vector
            self.polar = self.position_vector_polar(self.cartesian)
           
        if system == 'polar':
            self.polar = vector
            self.cartesian = self.position_vector_cartesian(self.polar)
            self.magnitud = vector[0]
            
    def position_vector_cartesian(self, polar):
        r, theta, phi = polar
        x = r * math.cos(theta) * math.sin(phi)
        y = r * math.sin(theta) * math.sin(phi)
        z = r * math.cos(phi)
        return [x,y,z]

    def position_vector_polar(self, cartesian):
        x, y, z = cartesian
        r = math.sqrt(x ** 2 + y ** 2 + z ** 2)
        if x!=0: theta = math.atan(y/x)
        else: theta = math.radians(90)
        phi = math.acos(z/r)
        
        return [r, theta, phi]
 
    
    def cartesian(self, value):
        self._cartesian = value
        self._polar = self.position_vector_polar(self._cartesian)
        self._x, self._y, self._z = self._cartesian
        self._r, self._theta, self._phi = self._polar


    def polar(self, value):
        self._polar = value
        self._cartesian  = self.position_vector_cartesian(self._polar)
        self._x, self._y, self._z = self.cartesian
        self._r, self._theta, self._phi = self.polar
    


# In[52]:


#Tests

vec1 = VectorCartesiano(1,1,7)
vec2 = VectorCartesiano(2,3,2)
# Creo una tercera intancia(implisitamente) y le asigno la suma de los objetos vec1 y vec2
vec3 = vec1 + vec2
# Creo una cuarta intancia(implisitamente) y le asigno la resta de los objetos vec1 y vec2
vec4 = vec1 - vec2

print(r"vec1 =", end=" ")
vec1.Print()
print(r"vec2 =", end=" ")
vec2.Print()
print("vec1 + vec2 =", end=" ")
vec3.Print()
print("vec1 - vec2 =", end=" ")
vec4.Print()
print(vec1.magnitud)

print(vec1 != vec2)
cr = vec1.Cruz(vec2)
cr.Print()

Vy =VectorPolar(1,8,20)
Vx =VectorPolar(1,1,1)

Vy.polar



