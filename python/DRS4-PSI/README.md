# DRSpy

Data analysis module for [DRS4 board](https://www.psi.ch/en/drs/evaluation-board).

**BETA** version. May not work 

---

## Installation

### Using pip

```console
user@host:~$ pip3 install DRSpy
```

### From source

```console
user@host:~$ python3 setup.py install
```

---

## Usage

Run `drspy --help` to see available options

```
Usage: drspy [OPTIONS]

Options:
  -f, --file TEXT       Choose input file  [required]
  -t, --type [txt|xml]  Choose input file formatting  [required]
  -e, --ext [png|pdf]   Output plot extension  [default: png]
  -r, --recursive TEXT  Load all [type] files e.g. ./main.py -e txt -r -f .
  --help                Show this message and exit.
```


## Examples

```console
user@host:~$ drspy -t txt -e pdf -f data.txt  
```
