
# coding: utf-8

# In[47]:


import numpy as np
import math as m


# In[199]:


def Factorial(n):
    if n<0 or n!=m.floor(n):
        print('¡Error! La función factorial solo admite enteros positivos mayores o iguales a cero.')
    else:
        value=1
        for i in range (1,n+1):
            value *=i
       
        return int(value)

             
    
def Binomial(n,r):
    if r>n or r<0 or r!=m.floor(r) or n!=m.floor(n):
        print('La función Binomial(n,r) solo admite enteros de r entre [0,n], con n mayor o igual a cero')
    else:
        value = Factorial(n)/(Factorial(r) * Factorial(n-r))
        return int(value)


# In[509]:


def Pascal(n):
    
    archivo = open('Pascal-n.txt.','w')

    for i in range(0,int(n)):
        
        T = np.zeros(i+1, dtype=int)       
        
        for j in range(0,int(i+1)):
            
            T[j] = Binomial(i,j)
        
        
        
        print('n = %.d ' %(i), end=' '*(int((2*n+6)*0.5-2*i)))
        g = str(T)
        g=g.replace(',','')
        g=g.replace('[','')
        g=g.replace(']','')
        separator = ' '    
        print(separator.join(g))
        archivo.write('n = %.d ' %(i) +' '*int((2*n+6)*0.5-2*i))
        archivo.write(separator.join(g)+'\n')
        
            
    
    return 
            
            
            
   


# In[514]:


#Pascal(5)


# In[503]:


def Pascal1(n):
    text = open('pt.txt','w')
    a=[]
    for i in range(n):
        a.append([])
        a[i].append(1)
        for j in range(1,i):
            a[i].append(a[i-1][j-1]+a[i-1][j])
        if(n!=0):
            a[i].append(1)
    for i in range(n):
        print('n = %.d'%(i), "   "*(n-i),end=" ",sep=" ")
        for j in range(0,i+1):
            print('{0:6}'.format(a[i][j]),end=" ",sep=" ")
            
        print()


# In[506]:


#Pascal1(10)

