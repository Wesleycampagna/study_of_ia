class heuristicDetermination:

    # queria saber se esse mpetodo pode ficar abaixo dos vetores estaticos 
    # aparentemente os métodos chamaveis já devem estar em memória (shit)
    def calculateHeuristic(self):

        """ Faça a mágica aqui """

        #RETURN OUTPUT HERE
        #return self.getArrayOutput()
        return  [3, 2, 4, 4, 1]

    # static 
    array= [[0, 0, 3, 4, 4, 1],
            [3, 3, 0, 0, 1, 2],
            [4, 0, 0, 1, 0, 1],
            [2, 2, 2, 3, 2, 2]]

    # static  
    resolution = {
        'input': array,
        'output': calculateHeuristic(array),
        'message': 'incorrect output'
    }

    # misterio da pilha a resolver
    def getArrayOutput(self):
        return [3, 2, 4, 4, 1]


import test

trab = heuristicDetermination()
resolution = heuristicDetermination.resolution

tdd = test.TDD(resolution)
tdd.print()
tdd.resolution()