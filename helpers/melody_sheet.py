#!/usr/bin/python3

from music21 import *

soc = {
    'n1' : 'C',
    'n2' : 'D',
    'n3' : 'E',
    'n4' : 'F',
    'n5' : 'G',
    'n6' : 'A',
    'n7' : 'B'
}

rules_before_final = {
    soc['n1']: (soc['n5'], soc['n4'], soc['n3'], soc['n2']),
    soc['n2']: (soc['n5'], soc['n6'], soc['n7'], soc['n1']),
    soc['n3']: (soc['n4'], soc['n1'], soc['n7'], soc['n6'], soc['n5']),
    soc['n4']: (soc['n2'], soc['n5'], soc['n6'], soc['n7'], soc['n1']),
    soc['n5']: (soc['n1'], soc['n2'], soc['n3'], soc['n4'], soc['n1']),
    soc['n6']: (soc['n3'], soc['n6']),
    soc['n7']: (soc['n5'], soc['n1']),
}