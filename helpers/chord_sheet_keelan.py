#!/usr/bin/python3

chord_sheet = {
    'one':['C2', 'C3', 'E3', 'G3'],
    'two':['D-2', 'D-3', 'F3', 'A-3'],
    'three':['E2', 'E3', 'G3', 'B-3'],
    'four':['F2', 'F3', 'A-3', 'C4'],
    'five':['G2', 'G3', 'B-3', 'D-4'],
    'six':['A-2', 'A-3', 'C4', 'E4'],
    'seven':['B-2', 'B-3', 'D-4', 'F4']
}

chord_rules = {
            'one': ('three', 'four', 'seven', 'one'),
            'two': ('six', 'five', 'four', 'two'),
            'three': ('one', 'two', 'four', 'three'),
            'four': ('five', 'six', 'three', 'four'),
            'five': ('two', 'one', 'six', 'five'),
            'six': ('four', 'seven', 'five', 'six'),
            'seven': ('one', 'two', 'six', 'seven'),
        }
        