import numpy as np
import matplotlib.pyplot as plt 
import math

#Simulacion de muestras cauchy alrededor de x_0

x_0 = 10 
delta = 10 #alejamiento de x_0 para restringir ejes del grafico
gamma = 1 
k=2500  #cant muestras
kk=250

#inicializacion de variables, van a ser las muestras simuladas
f_inv_cauchy_k = np.zeros(k)
f_inv_cauchy_k_2 = np.zeros(k)
f_inv_cauchy_kk = np.zeros(kk)
f_inv_cauchy_kk_2 = np.zeros(kk)

#Se obtienen los sets de muestras cauchy
for i in range(k):
    f_inv_cauchy_k[i]= gamma*(math.tan(math.pi*(np.random.random() - (1/2)))) + x_0
    f_inv_cauchy_k_2[i]= gamma*(math.tan(math.pi*(np.random.random() - (1/2)))) + x_0
for i in range(kk):
    f_inv_cauchy_kk[i]= gamma*(math.tan(math.pi*(np.random.random() - (1/2)))) + x_0
    f_inv_cauchy_kk_2[i]= gamma*(math.tan(math.pi*(np.random.random() - (1/2)))) + x_0    

#Calculo la media muestral
media_muestral_k = f_inv_cauchy_k.mean() #set 1 de k muestras
media_muestral_k_2 = f_inv_cauchy_k_2.mean() #set 2 de k muestras
media_muestral_kk = f_inv_cauchy_kk.mean() #set 1 de kk muestras
media_muestral_kk_2 = f_inv_cauchy_kk_2.mean() #set 2 de kk muestras

#Distribucion de las muestras
cauch_k = 1/(math.pi*gamma*(1+ ( (f_inv_cauchy_k-x_0)/gamma )**2 ))
cauch_k_2 = 1/(math.pi*gamma*(1+ ( (f_inv_cauchy_k_2-x_0)/gamma )**2 ))
cauch_kk = 1/(math.pi*gamma*(1+ ( (f_inv_cauchy_kk-x_0)/gamma )**2 ))
cauch_kk_2 = 1/(math.pi*gamma*(1+ ( (f_inv_cauchy_kk_2-x_0)/gamma )**2 ))

#Graficos de las muestras
plt.plot(f_inv_cauchy_kk,cauch_kk,'o',markersize=3,label="1) k=%d muestras: "%kk + "Media muestral = %.3f" %media_muestral_kk)
plt.plot(f_inv_cauchy_kk_2,cauch_kk_2,'o',markersize=3,label="2) k=%d muestras: "%kk + "Media muestral = %.3f" %media_muestral_kk_2)
plt.plot(f_inv_cauchy_k,cauch_k,'x',markersize=3,label="3) k=%d muestras: "%k + "Media muestral = %.3f" %media_muestral_k)
plt.plot(f_inv_cauchy_k_2,cauch_k_2,'x',markersize=3,label="4) k=%d muestras: "%k + "Media muestral = %.3f" %media_muestral_k_2)
plt.xlabel('muestras cauchy alrededor de x0=%d'%x_0)
plt.ylabel('p(x)')
plt.grid()
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', mode="expand", borderaxespad=0.)
plt.xlim((x_0-delta,x_0+delta)) #Me interesa ver que pasa alrededor de x_0
plt.show
#plt.savefig('muestras_cauchy.png',bbox_inches='tight')

