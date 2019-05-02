import numpy as np

def print_linscape():
    for element in x: 
        print( element )

# cria um array de um intervalo 'start' até 'end', com 'num' elements 
#numpy.linspace(start, stop, num = 50, endpoint = True, retstep = False, dtype = None)

# deste modo x receberá 50 elementos como padrão 
# x = np.linspace(1, 10)
# print_linscape()


# array de 1 a 10 com 10 posições. 
x = np.linspace(1, 10, 10)
print_linscape()

# considera numeros de 1 a 9.x, mas n o 10 
# x = np.linspace(1, 10, 10, False)
# print_linscape()

# retorna uma tupla com valores: tupla[0] = array de 10 pos de 1 a 10 e tupla[1] = gap entre os numeros
# x = np.linspace(1, 10, 10, True, True)
# print_linscape()
# print('--------------------------')
# print(x)

# ultimo não sei 
