class TDD:
    
    def __init__(self, resolution):
        self.array = resolution['input'];
        self.res = resolution['output']
        self.msg = resolution['message']

    def resolution(self):
        resol = self.res == [3, 2, 4, 4, 1]
        
        # in python todas as variaveis de classe devem ter self
        # variaveis de método não precisam
        """ print('resol: ', resol)
        print('res; ', self.res) """
        
        assert resol, self.msg

    def print2(self):
        print( 'more that')

    #testar o format
    def print(self):
        print ('deve aparecer a messagem :: {} ::. Is correct?'.format(self.msg,), self.res)
        self.print2()