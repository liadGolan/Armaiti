#!/usr/bin/python3

chord_sheet = {
    'one':['C2', 'C3', 'E-3', 'G3'],
    'two':['D2', 'D3', 'F3', 'A-3'],
    'three':['E-2', 'E-3', 'G3', 'B-3'],
    'four':['F2', 'F3', 'A-3', 'C4'],
    'five':['G2', 'G3', 'B-3', 'D4'],
    'six':['A-2', 'A-3', 'C4', 'E-4'],
    'seven':['B-2', 'B-3', 'D4', 'F4']
}

chord_rules = {
            'one': ('one', 'four', 'one', 'five'),
            'two': ('six', 'two', 'five', 'one'),
            'three': ('one', 'six', 'four', 'five'),
            'four': ('seven', 'four', 'two', 'five'),
            'five': ('six', 'four', 'five', 'one'),
            'six': ('one', 'three', 'four', 'five'),
            'seven': ('one', 'six', 'two', 'five'),
        }
        