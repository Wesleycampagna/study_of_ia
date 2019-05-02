import dataset as data
import matplotlib.pyplot as plt
import numpy

y_set = []
x_set = []

dataset = data.dataset4

for element in dataset:
    y_set.append(element[0])
    x_set.append(element[1])
    print (element)

teta_um = 1
teta_zero = 1
alpha = 0.0001
max_iteractions =  1000000
rounded = 7


# Ai => h(xi) = θzeroi + θumi * xi
def h_x (i):
    return teta_zero + teta_um * x_set[i]


# Bi => h(xi) - yi <=> Ai - yi 
# OR 
# Bi => (h(xi) - yi) * xi <=> (Ai - yi) * xi
def error_dset(i, is_teta_um):
    if is_teta_um:
        return (h_x(i) - y_set[i]) * x_set[i]

    return h_x(i) - y_set[i]

# teta_zero = 4 - 58.5 = -54.5

def sum_total(x=False):
    sum = 0

    for iterator in range(len(dataset)):
        sum += error_dset(iterator, x)

    return sum 


# θzero = θzero - alpha * 1 / tam_dataset * SOMATÓRIO (Bi)
def update_teta_zero():
    # print (teta_um)
    return round(teta_zero - alpha * (1/len(dataset)) * sum_total(x=False), rounded)


# θum = θum - alpha * 1 / tam_dataset * SOMATÓRIO (Bi * xi)
def update_teta_um():
    #print(teta_zero)
    return round(teta_um - alpha * (1/len(dataset)) * sum_total(x=True), rounded)
    

iterator = 0 
new_teta_um = 0
new_teta_zero = 0

while iterator <= max_iteractions and new_teta_um != teta_um:

    if iterator >= 1:
        teta_um = new_teta_um
        teta_zero = new_teta_zero

    new_teta_um = update_teta_um()
    new_teta_zero = update_teta_zero()

    print('teta zero: ', teta_zero, ' - teta um: ', teta_um, ' - i: ', iterator)

    iterator += 1

# cria um vetor com 'len(x_set)' elementos de '0' á maior posição do vetor ordenado
x_eq = numpy.linspace(0, x_set[-1], len(x_set))

# reta linear = θzero + θum * x  (reta que representa a melhor adaptação pro dataset)
reta_linear = teta_zero + teta_um * x_eq
#reta_linear = -0.072839 + 7.5926843 * x_eq
# print (x_eq)


plt.plot(x_set, y_set, label='f(x) = {0:9.5f} + {0:9.5f}x'.format(teta_zero, teta_um), marker='o', linestyle='none', markersize=1.5, color='lightblue')
plt.plot(x_eq, reta_linear, color='red', linewidth=0.4)
#plt.axis([0, 0.2, 0, 1.5])
plt.ylabel('y')
plt.xlabel('x')
plt.legend()
plt.show()
