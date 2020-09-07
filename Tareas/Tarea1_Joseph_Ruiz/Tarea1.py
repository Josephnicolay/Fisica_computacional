
# coding: utf-8

# In[40]:


import funciones as f

def probabilidad_moneda(n,k):
    P = f.Binomial(n,k)/(2**n)
    return P

    
    


# In[47]:


print('la probabilidad de que si se hace este experimento 100 veces, el resultado sean 10 veces cara es:','\n')
print((probabilidad_moneda(100,10)), '\n')

print('Y la probabilidad que caiga cara mas de 30 veces es: ', '\n')
suma = 0
for k in range (30,100+1):
    
    suma += probabilidad_moneda(100,k)
print(suma)

