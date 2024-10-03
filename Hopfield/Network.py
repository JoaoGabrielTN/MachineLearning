import numpy as np

class HopfieldNet:
    def __init__(self, neurons):
        self.__neurons = neurons
        self.__threshold = 0
        self.start()

    @property
    def neurons(self):
        return self.__neurons

    @neurons.setter
    def neurons(self, neurons):
        self.__neurons = neurons
    
    def start(self):
        self.__w = []
        length = range(len(self.__neurons))
        for i in length:
            self.__w.append([])
            for j in length:
                if i == j:
                    self.__w[i].append(0)
                else:
                    self.__w[i].append(1)
                   
    def see(self):
        print("Neuron states:\n")
        for i in self.__neurons:
            print(i, end=" ")
        print("\nConections:\n")
        for i in self.__w:
            for j in i:
                print(j, end=" ")
            print('\n')

    def update(self):
        length = range(len(self.__neurons))
        for i in length:
            weighted_sum = 0
            for j in length:
                weighted_sum = weighted_sum + self.__neurons[j]*self.__w[i][j]

            # Change this if/else for an activation function (heavyside)
            if weighted_sum > self.__threshold:
                self.__neurons[i] = 1
            else:
                self.__neurons[i] = 0

if __name__ == "__main__":
    net = HopfieldNet([1, 1, 0, 0])
    net.see()
    net.update()
    net.see()
