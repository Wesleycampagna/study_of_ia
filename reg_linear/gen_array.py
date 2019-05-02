import matplotlib.pyplot as plt
import random as rand


class generate_dataset:
    
    # improve further to pass in parameter constants and f(x)

    def __init__(self, show_plot=False):

        self.range_max_elements = 100            # quantidade maxima de elementos que entram no dataset
        self.random_gap_min_max = [0, 200]       # no eixo y quanto pode ser a subida ou queda dos elementos 
        self.limiar_x_accept = 0.6               # aceita apenas alguns x que forem maior que o limiar - random 
        self.show_plot = show_plot

        self.dataset = []
        self.y_set = []
        self.x_set = []

        self.create()


    def raffle_a_porcentual_value(self):
        return rand.randint(0, 100) / 100

    def add_y_set_plot(self, f_x):
        self.y_set.append(f_x)

    def add_x_set_plot(self, x):
        self.x_set.append(x)

    def show_plotmap(self):
        plt.plot(self.x_set, self.y_set, marker='o', label='data', color='#FF0000', markersize='0.8', linestyle='none')   
                                                            # add array y_set e x_set para abcissa e coordenadas
                                                            #   alem do label
        plt.ylabel('f(x) = (3/2)x + 4x')                    # nomenclatura y label 
        plt.xlabel('x')                                     # nomenclatura x label
        plt.legend()                                        # add label legend to plot
        plt.show()                                          # show the graph prot

    def create(self):
        for x in range (self.range_max_elements):
            
            f_x = (3/2)*x + 4*x            # formula da f(x)
            f_x += rand.randint(self.random_gap_min_max[0], self.random_gap_min_max[1])
            linha = [f_x, x]
            
            if self.raffle_a_porcentual_value() > self.limiar_x_accept:
                self.dataset.append(linha)
                self.add_y_set_plot(f_x)
                self.add_x_set_plot(x)

        for element in self.dataset:
            print (element)

        if self.show_plot:
            self.show_plotmap()


generate_dataset(show_plot=True)