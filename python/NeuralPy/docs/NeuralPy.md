# NeuralPy package

## Submodules

## NeuralPy.NeuralPy module


### class NeuralPy.NeuralPy.Network(inputs=2, neurons_per_layer=[2, 3, 1], learning_rate=0.5)
Bases: `NeuralPy.Neuron.Neuron`

—


#### \__init__(inputs=2, neurons_per_layer=[2, 3, 1], learning_rate=0.5)
Creating neuron with neuron_inputs+1 weights, the last one weight is bias.
You can change learning_rate later using set_learning_rate(x) method.


#### backpropagation_algorithm(learning_vector, expected_outputs)

#### draw()
Draw decision lines for 2D inputs


#### network_test()
random test


#### print_structure()
Show structure


#### run(input_vector)
Return neuron reply for input vector


#### training(learning_vectors, expected_vectors, learning_cycles)
Traning


#### training_from_file(path, learning_cycles)
FILE STRUCTURE:
Odd lines - learning inputs
Even lines - expected output
EXAMPLE:
0 1 0 1 0 0
1 1
1 2 1 0 1 1
0 2


### NeuralPy.NeuralPy.getrandbits(k)

### NeuralPy.NeuralPy.random()
## NeuralPy.Neuron module


### class NeuralPy.Neuron.Neuron(neuron_inputs=2, learning_rate=1.0)
Bases: `object`

Simple neuron model with two learning methods: delta rule and adaline.

Options:

In order to teach neuron from file, we must create text file with structure:
- Odd lines - learning vector e.g. 0 1 0 1..
- Even lines - expected answers e.g. 1
Example:
—xor.txt—
1 1

> 0

0 1
1
1 0
1
0 0
0 
————-
running: INSTANCE.learning_from_file(path, teaching_cycles, optional )

If you want check answer for l_vectors immediately, set up optional to ‘check’ .

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
- ‘sigmoid’
- ‘linear’

Code example:

>>n = 2#Number of connection
>>x = [[1,1],[0,1],[1,0]]#learning vectors
>>y = [1,0,0]#expected outpurts
>>c = 1000#learning cycles
>>neuron = Neuron(n)#creating instance with sigmoid activation function
>>neuron.set_learning_rate(0.2)#set learning rate
>>neuron.print_weights#showing current random weights
>>neuron.training(x,y,c,’check’)
>>neuron.draw()#showing decision line


#### \__init__(neuron_inputs=2, learning_rate=1.0)
Creating neuron with neuron_inputs+1 weights, the last one weight is bias.
You can change learning_rate later using set_learning_rate(x) method.


#### df_activ(x, beta=1.0)
Derivate of activation function


#### df_linear(x, beta=1.0)

#### draw()

#### f_activ(x, beta=1.0)
Sigmoid activation func.


#### f_linear(x, beta=1.0)

#### import_neuron(path='saved_last.neu')

#### learn_adaline(learning_vector, expected_output)
Single learning cycle (Adaline rule)


#### learn_delta(learning_vector, expected_output)
Single larning cycles for delta rule


#### print_weights()
Showing actual weights


#### reset_weights()
Setting random weights again.


#### run(\*inputs)
Calculation neuron answer.
This method gets input_vector with additional ‘1’ element for bias weight.


#### save_neuron(path='saved_last.neu')

#### set_f_activ(func='sigmoid')
Setting activation function.
Options:
- ‘sigmoid’
- ‘linear’


#### set_learning_rate(learning_rate)
Setting learning rate.


#### summ_signals(\*inputs)

#### temp_df()

#### temp_f()

#### training(learning_vectors, expected_outputs, n=1000, options='')
To teach the neuron form code:
Instance.training(learning_vestors, expected_vectors, teaching_cycles, optional)
Structure:
- learning vectors - [[1,0],[1,1],[0,1]]
- expected_vectors - [1,1,0]


#### training_from_file(path, n=1000, options='')
FILE STRUCTURE:
Odd lines - learning inputs
Even lines - expected output
EXAMPLE:
0 1 0 1 0 0
1
1 2 1 0 1 1
0

If traning file contains wrong data (for another neuron), this method should rebuild neuron to correct inputs.


### NeuralPy.Neuron.getrandbits(k)

### NeuralPy.Neuron.random()
## Module contents
