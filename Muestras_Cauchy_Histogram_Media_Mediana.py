import numpy as np
import matplotlib.pyplot as plt 
import math

#Simulacion de muestras cauchy alrededor de x_0


x_0 = 10 
x_02 = 40
delta = 10 #alejamiento de x_0 para restringir ejes del grafico
gamma = 1 
k=100  #cant muestras
f_inv_cauchy = np.zeros(k)
n=1000 #Cant de realizaciones
mediana = np.zeros(n)
media = np.zeros(n)
mediana2 = np.zeros(n)
media2 = np.zeros(n)
f_inv_cauchy = np.zeros(n)
f_inv_cauchy2 = np.zeros(n)

def inv_cauchy(a,g):
    cauchy_samp = g*(math.tan(math.pi*(np.random.random() - (1/2)))) + a
    return cauchy_samp

for i in range(n):
    for j in range(k):
        f_inv_cauchy[j]= inv_cauchy(x_0,gamma)
        f_inv_cauchy2[j]= inv_cauchy(x_02,gamma)
    mediana[i] = np.median(f_inv_cauchy)
    media[i] = np.mean(f_inv_cauchy)
    mediana2[i] = np.median(f_inv_cauchy2)
    media2[i] = np.mean(f_inv_cauchy2)


plot1 = plt.figure(1)
plt.hist(mediana,bins='auto')
plt.title('Histograma de la Mediana en %d realizaciones de '%n+'%d muestras'%k)
plt.xlabel('Mediana, x0=%d'%x_0)
plt.ylabel('Cantidad de ocurrencias')
plt.grid(axis='y', alpha=0.75)
plt.show
output_filename = 'mediana_x0=' + str(x_0) +'_n=' + str(n) + '.png'
#plt.savefig(output_filename,bbox_inches='tight')

plot2 = plt.figure(2)
plt.hist(mediana2,bins='auto')
plt.title('Histograma de la Mediana en %d realizaciones de '%n+'%d muestras'%k)
plt.xlabel('Mediana, x0=%d' %x_02)
plt.ylabel('Cantidad de ocurrencias')
plt.grid(axis='y', alpha=0.75)
plt.show
output_filename = 'mediana_x0=' + str(x_02) +'_n=' + str(n) + '.png'
#plt.savefig(output_filename,bbox_inches='tight')

plot3 = plt.figure(3)
plt.hist(media,bins='auto',label='x0=%d' %x_0)
plt.hist(media2,bins='auto',label='x0=%d' %x_02)
plt.title('Histograma de la Media en %d realizaciones de '%n+'%d muestras'%k)
plt.xlabel('Media')
plt.ylabel('Cantidad de ocurrencias')
#plt.xlim((-4,8)) 
plt.grid()
plt.legend()
plt.show
output_filename = 'media_n=' + str(n) + '.png'
#plt.savefig(output_filename,bbox_inches='tight')
