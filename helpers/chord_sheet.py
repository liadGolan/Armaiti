#!/usr/bin/python3

chord_sheet = {
    'one':['F2', 'F3', 'A3', 'C4'],
    'two':['G2', 'G3', 'B-3', 'D4'],
    'three':['A2', 'A3', 'C4', 'E4'],
    'four':['B-2', 'B-3', 'D4', 'F4'],
    'five':['C3', 'C4', 'E4', 'G4'],
    'six':['D3', 'D4', 'F4', 'A4'],
    'seven':['E3', 'E4', 'G4', 'B-4']
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
        