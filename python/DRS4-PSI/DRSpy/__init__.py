import os
import click
import  matplotlib
matplotlib.use("Agg")
import  matplotlib.pyplot as plt
import pandas as pd

from scipy.optimize import curve_fit

@click.command()
@click.option('-f','--file', '_file', help='Choose input file', required=True, type=str)
@click.option('-t','--type', '_ftype', help='Choose input file formatting', required=True, type=click.Choice(['txt', 'xml']))
@click.option('-e','--ext', '_ext', help='Output plot extension', default='png', type=click.Choice(['png', 'pdf']), show_default=True)
@click.option('-r', '--recursive', '_recursive', help='Load all [type] files e.g. ./main.py -e txt -r -f .')
def main(_ftype, _ext, _recursive, _file):
    if _ftype == 'txt':
        raise Exception("Function temporary unavailable")
    elif _ftype == 'xml':
        raise Exception("Function temporary unavailable")

if __name__ == '__main__':
    main()

