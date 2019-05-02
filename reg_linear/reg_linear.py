import dataset as data

y_set = []
x_set = []

dataset = data.dataset

for element in dataset:
    y_set.append(element[0])
    x_set.append(element[1])

teta_um = 1
teta_zero = 1
alpha = 0.05


# Ai => h(xi) = θzeroi + θumi * xi
def h_x (i):
    return teta_zero + teta_um * x_set[i]

# Bi => h(xi) - yi <=> Ai - yi or (h(xi) - yi) * xi <=> (Ai - yi) * xi
def error_dset(i, is_teta_um):
    if is_teta_um:
        k = (h_x(i) - y_set[i]) * x_set[i]
        print ('erro: ', k)
        return k

    return h_x(i) - y_set[i]

def somatorio(x=False):
    sum = 0

    for iterator in range(len(dataset)):
        sum += error_dset(iterator, x)

    print('sum: ', sum)

    sum = 2

    return sum 


# θzero = θzero - alpha * 1 / tam_dataset * SOMATORIO (Bi)
def update_teta_zero():
    # print (teta_um)
    new_teta_zero = teta_zero - alpha * (1/len(dataset)) * somatorio()
    print ('teta_zero: ', new_teta_zero)
    # teta_zero = new_teta_zero


# θum = θum - alpha * 1 / tam_dataset * SOMATORIO (Bi * xi)
def update_teta_um():
    #print(teta_zero)
    new_teta_um = teta_um - alpha * (1/len(dataset)) * somatorio(x=True)
    print ('teta_um: ', new_teta_um)
    #teta_um = new_teta_um

def update():
    update_teta_um()
    update_teta_zero()

iterator = 0 

while iterator < 1000:

    update()

    print('teta zero: ', teta_zero, ' - teta um: ', teta_um)

    iterator += 1
