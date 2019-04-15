set_objective = [(0, 0),(1, 1), (2,2), (3,3)]
setOfData = []
setOfCostFunction = []

# A ideia é testar  hipóteses e baseando na função de custo analisar quão distante 
# é do ideal. Usa-se teta_zero = 0 
teta_zero = 0

#função de custo
def cost(set, teta_um):
    #1/2*m * SOMATORIO(i até m) ( h(x^(i)) − y^(i))²
    costFunction = 0

    for element in range(len(set)):
        costFunction += ((set[element][1] - set_objective[element][1]) ** 2 )

    setOfCostFunction.append((teta_um, (1/(2*(len(set)- 1))) * costFunction))

#resultado de funços para delta
def setNewSetOfData(teta_um):
    setOfData.append(function(4, teta_um))
    pass

#percorre 'num_iterator' vezes x
def function(num_iterator, teta_um):

    setTeta = []
    
    for i in range(num_iterator):
        # h (x^(i)) = θ(zero) + θ(um) * x ^(i)   
        setTeta.append((i, (teta_zero + teta_um * i)))
    
    cost(setTeta, teta_um)
    
    return setTeta

#hipótese #1 -> θ(um) = 0
teta_um = 0
setNewSetOfData(teta_um)

#hipótese #2 -> θ(um) = 0.5
teta_um = 0.5
setNewSetOfData(teta_um)

#hipótese #3 -> θ(um) = 1
teta_um = 1
setNewSetOfData(teta_um)

setNewSetOfData(1.5)
setNewSetOfData(2)

#print of data
print('setOfData: ', setOfData)

print('------------------------------')

#print of cost
print('setOfCostFunction: ', setOfCostFunction)

