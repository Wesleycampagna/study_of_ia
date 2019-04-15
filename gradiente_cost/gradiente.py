""" A ideia e fazer o gradiente para 2x^3 + 3x^2 + 2 """

#base foi deste rapaz: https://github.com/codificandobits/Programacion_Gradiente_Descendente_en_Python/blob/master/gradiente_descendente.py


import matplotlib.pyplot as plt
from numpy import linspace

#teta_jota = teta_jota - alpha  * termo de derivacao --> formula 

#logo a derivada para a funcao e 3*2x^2 + 2*3x + 3 = 6x^2 + 6x (flutua muita casa nao da)

teta_jota = 100
alpha = 0.0095                   #alpha's para teste = 1.0, 0.15 0.025 0.0025
#iterations = 1000
casas_decimais = 7

it = []
y = []

def grad_(it, y_v):
    global casas_decimais, teta_jota, alpha

    iterator = 0
    new_teta_jota = teta_jota
    old_teta_jota = teta_jota -1        #diferente pra entra no while
   
    #for i in range (iterations):
    while new_teta_jota != old_teta_jota:

        # f(x) e sua derivada -> onde é x substitui por 'new_teta_jota'
        f_x = round(new_teta_jota**2 + 1, casas_decimais)
        derivada = 2*new_teta_jota

        old_teta_jota = new_teta_jota
        new_teta_jota = round(new_teta_jota - alpha * derivada, casas_decimais)
        print('x: ', new_teta_jota, 'f(x): ', f_x, 'x$: ', old_teta_jota) 


        y_v.append(f_x)
        it.append(iterator+1)

        iterator += 1

        if iterator == 1000:
            print('\n--> NAO CONVERGIU EM 1000 TENTATIVAS!')
            break

    return iterator


iterations = grad_(it, y)

plt.subplot(1, 2, 1)
plt.plot(it, y)
plt.xlabel('x')
plt.ylabel('f(x)')

X = linspace(-3,3,iterations)
Y = X**2 + 1
plt.subplot(1,2,2)
plt.plot(X,Y,0.0,1.0,'ro')
plt.xlabel('x')
plt.ylabel('y')
plt.show()



#(((6*x) ** 2) + (6*x) + 3)
"""     SERIA EQUIVALENTE 
        f_x = round((((2*new_teta_jota) **3) + ((3*new_teta_jota) ** 2) + 3), 4)
        derivada = round((((6*new_teta_jota) **2) + (6*new_teta_jota)), 4) """
