import getopt
import sys

# : and = expect value
o,a = getopt.getopt(sys.argv[1:],'abch:',['help=','run'])

for i,j in o:
    print('{}->{} '.format(i,j))
