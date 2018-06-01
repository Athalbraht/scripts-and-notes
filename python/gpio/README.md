# GPIO

python wrapper for wiringpi

### installing

```python3 setup.py install```

### Runing as module

```python
import gpio

pins = gpio.init("output", 1, 2) #initialize pins 1&2 in output mode
pins.add('input', 8,9) #adding pins 8&9 as input

pins.set(1, 1, 2) # voltage up on pins 1 and 2
pins.set(0, 2) #voltage down on pin 2

state = pins.value(8,9) #getting info from pins 8 and 9  

```

### Running from command line

**TODO**

- [x] mm
- [] cmm
- [] addo
