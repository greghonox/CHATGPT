from os import getcwd
from os.path import join

TOKEN_API = ''

with open(join(getcwd(), 'scripts', '.token'), 'r') as f:
    TOKEN_API = f.read()