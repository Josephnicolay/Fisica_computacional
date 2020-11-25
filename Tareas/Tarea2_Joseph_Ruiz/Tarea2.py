
# coding: utf-8

# In[58]:


from vector import VectorCartesiano, VectorPolar
import math as m


# Consideremos los siguientes tres vectores dados en la base cartesiana
# 
# 
# $$ \textbf{a} = [ 1.5 , 0 , 2.04 ]$$
# $$ \textbf{b} = [ 0 , 1 , 9]$$
# $$ \textbf{c} = [ 4.2 , 0.05 , 0] $$
# 

# Calculemos su forma en coordenas esféricas

# In[59]:


a = VectorPolar(1.5,0,2.04, system='cartesian')
b = VectorPolar(0,1,9, system='cartesian')
c = VectorPolar(4.2,0.05,0, system='cartesian')

print('Vector a = ', end=' ')
a.Print()
print('Vector b = ', end=' ')
b.Print()
print('Vector c = ', end=' ')
c.Print()


# In[60]:


print(r'Forma esférica es a = ', end=' ')
print(a.polar)
print(r'Forma esférica es b = ', end=' ')
print(b.polar)
print(r'Forma esférica es c = ', end=' ')
print(c.polar)


# Calculemos los productos internos de a,b,c

# In[61]:


print('(a|b) = ', end=' ')
print(a*b)
print('(a|c) = ', end=' ')
print(a*c)
print('(b|c) = ', end=' ')
print(b*c)


# Calculemos los productos vectoriales 

# In[62]:


print('a x b =', end=' ')
a.Cruz(b).Print()
print('a x c =', end=' ')
a.Cruz(c).Print()
print('b x c =', end=' ')
b.Cruz(c).Print()


# Calculculemos el angulo entre un par de vectores

# In[86]:


#Definase la funcion angulo_separacion
#Retorna 

def angulo_separacion(x,y):
    '''Retorna el angulo de separacion entre dos vectores medido en radianes'''
    #x, y instanciados por la clase VectorCartesiano(values) o VectorPolar (values, system='cartesian')
    return float(m.acos((x*y)/(x.magnitud*y.magnitud)))
angulo_separacion.__doc__


# In[87]:


print('El angulo entre a y b es %.2f rad'%(angulo_separacion(a,b)))

print('El angulo entre a y c es %.2f rad'%(angulo_separacion(a,c)))

print('El angulo entre b y c es %.2f rad' %(angulo_separacion(b,c)))

