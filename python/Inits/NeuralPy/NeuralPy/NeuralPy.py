#!/usr/bin/env python3


##################################
# File name: ann.py              #
# Author: Albert Szadziński      #
##################################

from random import uniform,randint
from numpy import dot, linspace
from .Neuron import *

class Network(Neuron):
    '''
    ---
    '''
    def __init__(self,inputs=2, neurons_per_layer = [2,3,1], learning_rate=0.5):
        self.layers = []#List for neurons
        self.learning_rate = learning_rate
        self.inputs = [inputs]+neurons_per_layer
        self.connections = inputs
        temp = 0
        for layer in neurons_per_layer:#filling list of neurons
            self.layers.append([ Neuron(self.inputs[temp]) for i in range(layer)])
            temp += 1
    
    #=========================Customize================================        
    def network_test(self):
        '''
        random test
        '''
        input_vector = [uniform(-1,1) for i in range(self.connections)]
        print('Network answer: ',self.run(input_vector))
        
    def print_structure(self):
        '''
        Show structure
	    '''
        temp = 0
        for layer in self.layers:
            print('\n============ {} LAYER ==========='.format(temp))
            for neuron in layer:#naming neu.
                nick = 'Neuron in {} layer with {} inputs, errors {}'.format(temp, len(neuron.weights)-1,neuron.delta)
                print(nick)
                neuron.id = nick
            temp += 1    
        print('\n')
        
    #======================Run & learning=================================    
    def run(self, input_vector):
        '''
        Return neuron reply for input vector
        '''
        layer_answers = []
        counter = 0
        for layer in self.layers:
            if counter != 0:
                layer_answers.append([neuron.run(layer_answers[counter-1]+[1]) for neuron in layer])
            elif counter == 0:
                layer_answers.append([neuron.run(input_vector+[1]) for neuron in layer])
            counter += 1
        return layer_answers[-1]    
    
    def backpropagation_algorithm(self, learning_vector, expected_outputs):
        error = []
        temp = 1
        counter = 0#counting layers
        
        for layer in self.layers[::-1]:

            if temp != 1:
                error.append([])
                counter_2 = 0#counting weights in previous layer
                for neuron in layer:
                    s = 0
                    counter_3 = 0#counting neurons in previous layer
                    for err in error[counter-1]:
                        s += err*self.layers[-counter][counter_3].weights[counter_2][0]#calc. errors
                        counter_3 += 1
                    error[counter].append(s)
                    counter_2 += 1
            elif temp == 1:
                temp = 0
                error.append([])
                counter_2 = 0
                for out in expected_outputs:
                    error[counter].append(out - self.run(learning_vector)[counter_2])#calc. errors for last layer
                    counter_2 += 1
            counter += 1
            
        #merging errors with neurons   
        counter_4 = 0
        for layer in self.layers[::-1]:
            counter_5 = 0
            for neuron in layer:
                neuron.delta = error[counter_4][counter_5] 
                counter_5 += 1
            counter_4 += 1
            
        #Updating weights
        layers_answers = [learning_vector]
        counter_1 = 0 #counting layers 
        for layer in self.layers:
            layers_answers.append([])
            for neuron in layer:
                vec = layers_answers[counter_1] + [1]
                answer = neuron.run(vec)
              #  print('\na-',answer)
                layers_answers[counter_1 + 1].append(answer)
                signal = neuron.summ_signals(vec)
                ds = neuron.temp_df(signal)
               # print('ds',ds)
              #  print('s-',signal)
               # print('d',neuron.delta)
                counter_2 = 0
                for weight in neuron.weights:
                   # print('w',weight[0])
                    o = self.learning_rate*neuron.delta*ds*vec[counter_2]
                   # print('o',o)
                    weight[0] += o                   
                    counter_2 += 1
            counter_1 += 1
    
    def training(self,learning_vectors, expected_vectors,learning_cycles):
        '''
        Traning
        '''
        for i in range(learning_cycles):
            for j in range(len(learning_vectors)):
                self.backpropagation_algorithm(learning_vectors[j],expected_vectors[j])                
                
    def draw(self):#Visualization of decision line for 2-inputs network
        '''
        Draw decision lines for 2D inputs
        '''
        import matplotlib.pyplot as plt
        X = linspace(-0.1,1.1,200)
        Y = linspace(-0.1,1.1,200)
        z=[]
        for i in range(len(X)):
            z.append([])
            for j in range(len(Y)):
                z[i].append(self.run([X[i],Y[j]])[0])

        X,Y = np.meshgrid(X,Y)
        Z = np.array(z)
        plt.contourf(X,Y,z)
        plt.plot([1,1,0,0,0.3,0.3,0.7,0.7,0.3,0.7,0.5,0.5],[0,1,0,1,0.3,0.7,0.3,0.7,0.5,0.5,0.3,0.7],'wo',[0.5],[0.5],'ro')#points
        plt.xlim(-0.1,1.1)
        plt.ylim(-0.1,1.1)
        plt.title('Decision line')
        #plt.grid(True)
        plt.show()          
                            
    def training_from_file(self,path,learning_cycles):
        '''FILE STRUCTURE:
        Odd lines - learning inputs
        Even lines - expected output
        EXAMPLE:
        0 1 0 1 0 0
        1 1
        1 2 1 0 1 1
        0 2
        '''
        with open(path, 'r') as file:
            temp_list = file.readlines()
            print('\nLoading {} examples...'.format(int(len(temp_list)/2)))    
            print('-->Loading learning vectors...')
            learning_vectors = [list(map(lambda x:float(x),i.split())) for i in temp_list[::2]]
            print('---->DONE')
            print('-->Loading expected vectors...')
            expected_vectors = [list(map(lambda x:float(x),i.split())) for i in temp_list[1::2]]
            print('---->DONE')
            print('DATA IMPORTED\n')
            self.training(learning_vectors, expected_vectors, learning_cycles)
	
	
	
	
	
	
		        

if __name__=="__main__":
    
#==============Neuron module test====================  
    '''
    n=Neuron(2)
    n.print_weights()
    expected_i = [[1,1],[1,0],[0,1],[0,0]]
    expected_o = [1,1,1,0]
    #n.training(expected_i,expected_o,10000,'check')
    n.training_from_file('or.txt',1000,'check')
    n.draw()
    del n
    '''                   

#=============Network module test======================
    import time as t
    learning_vectors = [[1,0],[0,1],[1,1],[0,0],[0.3,0.3],[0.3,0.7],[0.7,0.3],[0.7,0.7],[0.5,0.5],[0.5,0.6],[0.3,0.5],[0.7,0.5],[0.5,0.7],[0.5,0.3]]
    expected_vectors = [[0],[0],[0],[0],[0],[0],[0],[0],[1],[1],[0],[0],[0],[0]]
    learning_cycles = 400
    learning_rate = 0.3
    inputs = 2
    network_structure = [4,2,1]
    
    ann = Network(inputs,network_structure,learning_rate)

    ann.training(learning_vectors,expected_vectors,learning_cycles)

    ann.draw() 
    #ann.run([1,1])     
