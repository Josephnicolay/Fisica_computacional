
# coding: utf-8

# # Tarea 3: Numpy, Matplotlib & scipy
# 
# 
# Estudiante Joseph Nicolay Ruiz Alvarez - FCEN Universidad de Antioquia
# 
# ## Introdución
# 
# ### Punto 1
# 
# Una masa es suspendida de un resorte de constante k. La masa se desplaza del equilibrio por una distancia y0 y se suelta. Grafique la posicion Vs el tiempo, para al menos 5 conjuntos de parametros.
# 
# ## Punto 2 
# Cree una clase OsciladorAmortiguado con el fin de reproducir los dos puntos anteriores para un oscilador amortiguado. Asuma el caso subamortiguado.
# 
# ## Plus
# Considere el caso forzado y proceda de manera similar a los incisos anteriores

# In[1]:


# Importamos el modulo donde se construyo la Oscilador

## NOTA: esta clase posee los atributos y modulos necesarios para realizar el caso  general 
## del oscilador armónico forzado y amortiguado

import MasaResorte as mr
import numpy as np


# In[2]:


# punto 1

#vector de masa
m = np.array([1,2,3,4,5])

#frecuencias naturales
w_0 = np.array([1,0.2,2,4.2,3.5])

#Posiones iniciales
y_0 = np.array([1,1.5,4,2,2.5])
v_0 = np.array([0,1,0,4,2])

for i in range(0,5):
    Os_armonic = mr.Oscilador(masa=m[i],frec_natural=w_0[i])
    print('Oscilador con:')
    print('masa =', end = ' ')    
    print(Os_armonic.mass)    
    print('frecuencia = ', end=' ')
    print(Os_armonic.w_natural)
    
    Os_armonic.plot_solution(y_0[i],v_0[i])
   


# In[3]:


# punto 2

viscos = np.array([0.2,1,0.5,0.05,0.06])


for i in range(0,5):
    Os_armonic = mr.Oscilador(frec_natural=w_0[i],visco= viscos[i])
    print('Oscilador con:')
    print('masa =', end = ' ')    
    print(Os_armonic.mass)    
    print('frecuencia = ', end=' ')
    print(Os_armonic.w_natural)
    print('coeficiene lambda viscosidad = ', end=' ')
    print(Os_armonic.visc)
    
    Os_armonic.plot_solution(y_0[i],v_0[i])
   
    


# In[4]:


# Plus

w = np.array([1.3,2.4,0.8,4.2,4])
A_forzante = np.array([1,2,4,1.5,5])

for i in range(0,5):
    Os_armonic = mr.Oscilador(frec_natural=w_0[i], visco=viscos[i], frec_forzada= w[i], amplitud_forzada=A_forzante[i])
    print('Oscilador con:')
    print('masa =', end = ' ')    
    print(Os_armonic.mass)    
    print('frecuencia natural = ', end=' ')
    print(Os_armonic.w_natural)
    print('coeficiene lambda viscosidad = ', end=' ')
    print(Os_armonic.visc)
    print('Amplitud de la forzante = ', end=' ')
    print(Os_armonic.amplitud_f)
    print('frecuencia forzante = ', end=' ')
    print(Os_armonic.w_forzada)
    
    Os_armonic.plot_solution(y_0[i],v_0[i])
   

