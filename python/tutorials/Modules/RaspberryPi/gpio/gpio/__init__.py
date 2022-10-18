
from subprocess import check_output

class init():
    def __init__(self, direction, *gpio):
        self.gpio = {'output':set(), 'input':set()}
        self.mode(direction, gpio)

    def mode(self, direction, gpio):
        _gpio = set()
        try:
            for pin in gpio:
                check_output('gpio mode {} output'.format(pin), shell=True)
                _gpio.add(pin)
        finally:
            pass
        if direction == 'input':
            self.gpio['output'] -= _gpio
            self.gpio['input'] |= _gpio 
        elif direction == 'output':
            self.gpio['input'] -= _gpio
            self.gpio['output'] |= _gpio
        else:
            print("Wrong direction param")
        return None

    def value(self, *gpio):
        return [ int(check_output('gpio read {}'.format(pin), shell=True)) for pin in gpio ] 

    def set(self, _value,  *gpio):
        if len(self.gpio['output'] | set(gpio)) > len(self.gpio['output']):
            print('''Error: {} pins was not declared or doesn't exits'''.format(set(gpio) - self.gpio['output']))
            return None
        for pin in gpio:
            check_output('gpio write {} {}'.format(pin, _value), shell=True)
        return None
    
    def add(self, direction, *gpio):
        self.mode(direction, gpio)
        return None
