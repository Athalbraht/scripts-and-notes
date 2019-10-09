#!/usr/bin/env python3


##################################
# File name: ann.py              #
# Author: Albert Szadziński      #
##################################

from random import uniform,randint
from math import exp
import numpy as np
from numpy import dot, linspace

'''-------------------------------------------------------'''
class Neuron(): 
    '''
    Simple neuron model with two learning methods: delta rule and adaline.
    
    Options:
    
    In order to teach neuron from file, we must create text file with structure:
    - Odd lines - learning vector e.g. 0 1 0 1..
    - Even lines - expected answers e.g. 1
    Example:
    ---xor.txt---
    1 1
     0
    0 1
    1
    1 0
    1
    0 0
    0 
    -------------
    running: INSTANCE.learning_from_file(path, teaching_cycles, optional )
    
    If you want check answer for l_vectors immediately, set up optional to 'check' .
    

    
    To teach the neuron form code:
    Instance.training(learning_vestors, expected_vectors, teaching_cycles, optional)
    Structure:
    - learning vectors - [[1,0],[1,1],[0,1]]
    - expected_vectors - [1,1,0]
    
    Stimulating neuron:
    Instance.run([1,1]) or Instance.run(1,2,3)
    
    Changing activ_function:
    Instance.set_f_activ(option)
    options:
    - 'sigmoid'
    - 'linear' 
    
    Code example:
    
    >>n = 2#Number of connection
    >>x = [[1,1],[0,1],[1,0]]#learning vectors
    >>y = [1,0,0]#expected outpurts
    >>c = 1000#learning cycles
    >>neuron = Neuron(n)#creating instance with sigmoid activation function
    >>neuron.set_learning_rate(0.2)#set learning rate
    >>neuron.print_weights#showing current random weights
    >>neuron.training(x,y,c,'check')
    >>neuron.draw()#showing decision line
    '''
    
    def __init__(self, neuron_inputs=2, learning_rate=1.): 
        '''
        Creating neuron with neuron_inputs+1 weights, the last one weight is bias.
        You can change learning_rate later using set_learning_rate(x) method.
        '''       
        self.learning_rate = learning_rate        
        self.weights = []
        for i in range(neuron_inputs+1):
            self.weights.append([uniform(-1,1)])
            
        self.f='sigmoid'
        self.set_f_activ(self.f)
        
        self.beta = 1.#Slope factor
        #options for network
        self.id = ''#Neuron ID
        self.delta = 0 #error to multilayers neuralnetwork  
        self.momentum = 0  
            
#================Customize methods==================            
    def set_learning_rate(self,learning_rate):
        '''
        Setting learning rate.
        '''
        self.learning_rate = learning_rate
    
    def set_f_activ(self, func='sigmoid'):
        '''
        Setting activation function.
        Options:
        - 'sigmoid'
        - 'linear'
        '''
        if func == 'sigmoid':
            self.temp_f = self.f_activ
            self.temp_df = self.df_activ
            self.f = 'sigmoid'
        elif func == 'linear':
            self.temp_f = self.f_linear
            self.temp_df = self.df_linear
            self.f = 'linear'
        else:        
            print('Unknown function name\nsetting sigmoid function')
            self.temp_f = self.f_activ
            self.temp_df = self.df_activ
            self.f = 'sigmoid'
            
    def reset_weights(self):
        '''
        Setting random weights again.
        '''
        self.__init__(len(self.weights)-1)
        
    def print_weights(self): 
        '''
        Showing actual weights'''
        print(self.weights)

    def draw(self):#Visualization of decision line for 2-inputs neuron
        if len(self.weights) != 3:
            print('draw() option only for 2-inputs neuron')
            return None
        import matplotlib.pyplot as plt
        X = linspace(-0.1,1.1,200)
        Y = linspace(-0.1,1.1,200)
        f = lambda x: -(x*self.weights[1][0])/self.weights[0][0] - self.weights[2][0]/self.weights[0][0]
        Z = lambda x,y: dot([x,y,1],self.weights)
        z=[]
        for i in range(len(X)):
            z.append([])
            for j in range(len(Y)):
                z[i].append(self.run(X[i],Y[j],1))
        X,Y = np.meshgrid(X,Y)
        Z = np.array(z)
        plt.contourf(X,Y,z)
        plt.plot([0,0,1,1],[0,1,0,1],'wo')
        plt.xlim(-0.1,1.1)
        plt.ylim(-0.1,1.1)
        plt.title('Decision line')
        plt.grid(True)
        plt.show()
        
    def save_neuron(self,path='saved_last.neu'):
        with open(path,'w') as file:
            file.write('inputs:\n')
            file.write(str(len(self.weights)-1)+'\n')
            file.write('learning rate:\n')
            file.write(str(self.learning_rate)+'\n')
            file.write('weights:\n')
            file.write(str(self.weights)+'\n')
            file.write('activ_f:\n')
            file.write(str(self.f))
            print('\nSaved to {}\n'.format(path))
    
    def import_neuron(self,path='saved_last.neu'):
        with open(path,'r') as file:
            temp = file.readlines()
            temp_list = temp[1::2]
            self.__init__(int(temp_list[0][:-1]),float(temp_list[1][:-1]))
            self.weights = eval(temp_list[2][:-1])
            self.set_f_activ(temp_list[3])
            print('\nImported from {}\n'.format(path))
            
            
#===============Activation functions==================            
    def f_activ(self, x, beta=1.): 
        '''
        Sigmoid activation func.
        '''
        return 1/(1+exp(-x*beta))

    def df_activ(self, x,beta=1.):
        '''Derivate of activation function'''
        return self.f_activ(x)*(1 - self.f_activ(x))*beta
        
    def f_linear(self, x, beta=1.):
        return x*beta
        
    def df_linear(self, x, beta=1.):
        return beta
        
    def temp_f(self):pass
    def temp_df(self):pass

#=============Learning & stimulating====================    
    def summ_signals(self,*inputs):
        inp = list(inputs)
        return float(dot(inp, self.weights))

    def run(self, *inputs):#Calc. neuron answer [x1,....,xn,1]    
        '''
        Calculation neuron answer.
        This method gets input_vector with additional '1' element for bias weight.
        '''
        inp = list(inputs)
        return float(self.temp_f(dot(inp, self.weights),self.beta))

    def learn_delta(self, learning_vector, expected_output):
        '''
        Single larning cycles for delta rule
        '''      
        reply = self.run(learning_vector)   
        error = expected_output - reply
        
        for i in range(len(self.weights)):#Updating weights
            self.weights[i][0] += error*self.temp_df(self.summ_signals(learning_vector),self.beta)*learning_vector[i]*self.learning_rate
            
    def learn_adaline(self, learning_vector, expected_output):
        '''
        Single learning cycle (Adaline rule)  
        '''        
        error = expected_output - self.summ_signals(learning_vector)
        
        for i in range(len(self.weights)):#Updating weights
            self.weights[i][0] += error*self.temp_df(self.summ_signals(learning_vector),self.beta)*learning_vector[i]*self.learning_rate
    
    def training(self, learning_vectors, expected_outputs, n=1000, options=""):  
        '''
        To teach the neuron form code:
        Instance.training(learning_vestors, expected_vectors, teaching_cycles, optional)
        Structure:
        - learning vectors - [[1,0],[1,1],[0,1]]
        - expected_vectors - [1,1,0]        
            '''        
        for i in range(len(learning_vectors)):#adding input for bias
            learning_vectors[i].append(1)
            
        for i in range(n):
            for j in range(len(learning_vectors)):#Relaying all learning_data to learn()function
                self.learn_delta(learning_vectors[j], expected_outputs[j])

        if 'check' in options:#checking neuron anwsers after traning for learning_vec
            for j in range(len(learning_vectors)):
                print("Result for {} (expected {})-> ".format(learning_vectors[j][:-1], 
                                                              expected_outputs[j]),self.run(learning_vectors[j]))
                               
    def training_from_file(self, path, n=1000, options=""):#Loading learn_data from file
        '''FILE STRUCTURE:
        Odd lines - learning inputs
        Even lines - expected output
        EXAMPLE:
        0 1 0 1 0 0
        1
        1 2 1 0 1 1
        0
        
        If traning file contains wrong data (for another neuron), this method should rebuild neuron to correct inputs.
        '''
        with open(path, 'r') as file:
            temp_list = file.readlines()
            print('\nLoading {} examples...'.format(int(len(temp_list)/2)))    
            print('-->Loading learning vectors...')
            learning_vectors = [list(map(lambda x:float(x),i.split())) for i in temp_list[::2]]
            print('---->DONE')
            print('-->Loading expected outputs...')
            expected_outputs = [float(i.split()[0]) for i in temp_list[1::2]]
            print('---->DONE')
            print('DATA IMPORTED\n')
        
            if len(self.weights)-1 == len(learning_vectors[0]):
                self.training(learning_vectors, expected_outputs, n, options)
            else:
                print("Error: Current neuron with {} inputs, {}-inputs neuron in file".format(len(self.weights)-1, len(learning_vectors[1])))
                print("Changing neurontype to {}-inputs...\n".format(len(learning_vectors[0])))
                self.__init__(len(learning_vectors[0]))
                self.training(learning_vectors, expected_outputs, n, options)

