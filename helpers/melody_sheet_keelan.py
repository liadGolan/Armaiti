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

soc_in_key = {
    'n1' : 'C',
    'n2' : 'D-',
    'n3' : 'E',
    'n4' : 'F',
    'n5' : 'G',
    'n6' : 'A-',
    'n7' : 'B-'
}

rules_before_final = {
    soc['n1']: (soc['n6'], soc['n4'], soc['n5']),
    soc['n2']: (soc['n2'], soc['n6'], soc['n4'], soc['n3'], soc['n6'], soc['n1']),
    soc['n3']: (soc['n5'], soc['n6'], soc['n3'], soc['n1'], soc['n5'], soc['n6'], soc['n1']),
    soc['n4']: (soc['n7'], soc['n2'], soc['n3'], soc['n4']),
    soc['n5']: (soc['n6'], soc['n4'], soc['n2'], soc['n5'], soc['n3'], soc['n2']),
    soc['n6']: (soc['n4'], soc['n3'], soc['n2'], soc['n1']),
    soc['n7']: (soc['n3'], soc['n7'], soc['n2']),
}

## tuple structure (note,length,octave)
## each rule is split into two arrays one for each chord
rules_before_final_for_generation = {
    soc['n1']: [
        [
            (soc['n6'],1,5), 
            (soc['n4'],1,5)
        ],
        [
            (soc['n5'],2,5), 
        ]
    ],
    soc['n2']: [
        [
            (soc['n2'],.5,6), 
            (soc['n6'],.5,6),
            (soc['n4'],1,6)
        ],
        [
            (soc['n3'],1,6), 
            (soc['n6'],.5,5),
            (soc['n1'],.5,5)
        ]
    ],
    soc['n3']: [
        [
            (soc['n5'],.5,6), 
            (soc['n6'],.5,6), 
            (soc['n3'],.5,6),
            (soc['n1'],.5,6)
        ],
        [
            (soc['n5'],1,5),  
            (soc['n6'],.5,5),
            (soc['n1'],.5,6)
        ]
    ],
    soc['n4']: [
        [
            (soc['n7'],1,5),
            (soc['n2'],1,6), 
        ],
        [
            (soc['n3'],1.5,6), 
            (soc['n4'],.5,6)
        ]
    ],
    soc['n5']: [
        [
            (soc['n6'],1.5,6), 
            (soc['n4'],.5,6)
        ],
        [ 
            (soc['n2'],.5,6), 
            (soc['n5'],.5,6), 
            (soc['n3'],.5,6),
            (soc['n2'],.5,6)
        ]
    ],
    soc['n6']: [
        [
            (soc['n4'],1.5,5),
            (soc['n3'],.5,5)
        ],
        [ 
            (soc['n2'],1.5,6),
            (soc['n1'],.5,6)
        ]
    ],
    soc['n7']: [
        [
            (soc['n3'],1.5,5),
            (soc['n7'],.5,5)
        ],
        [
            (soc['n2'],2,6)
        ]
    ]
}

n1measure = stream.Measure()
n1measure.append(note.Note('A-5', quarterLength=1))
n1measure.append(note.Note('F5', quarterLength=1))
n1measure.append(note.Note('G5', quarterLength=2))

n2measure = stream.Measure()
n2measure.append(note.Note('D-5', quarterLength=.5))
n2measure.append(note.Note('A-5', quarterLength=.5))
n2measure.append(note.Note('F6', quarterLength=1))
n2measure.append(note.Note('E6', quarterLength=1))
n2measure.append(note.Note('A-5', quarterLength=.5))
n2measure.append(note.Note('C5', quarterLength=.5))

n3measure = stream.Measure()
n3measure.append(note.Note('G6', quarterLength=.5))
n3measure.append(note.Note('A-6', quarterLength=.5))
n3measure.append(note.Note('E6', quarterLength=.5))
n3measure.append(note.Note('C6', quarterLength=.5))
n3measure.append(note.Note('G5', quarterLength=1))
n3measure.append(note.Note('A-5', quarterLength=.5))
n3measure.append(note.Note('C6', quarterLength=.5))

n4measure = stream.Measure()
n4measure.append(note.Note('B-5', quarterLength=1))
n4measure.append(note.Note('D-6', quarterLength=1))
n4measure.append(note.Note('E6', quarterLength=1.5))
n4measure.append(note.Note('F6', quarterLength=.5))

n5measure = stream.Measure()
n5measure.append(note.Note('A-6', quarterLength=1.5))
n5measure.append(note.Note('F6', quarterLength=.5))
n5measure.append(note.Note('D-6', quarterLength=.5))
n5measure.append(note.Note('G6', quarterLength=.5))
n5measure.append(note.Note('E6', quarterLength=.5))
n5measure.append(note.Note('D-6', quarterLength=.5))

n6measure = stream.Measure()
n6measure.append(note.Note('F5', quarterLength=1.5))
n6measure.append(note.Note('E5', quarterLength=.5))
n6measure.append(note.Note('D-6', quarterLength=1.5))
n6measure.append(note.Note('C6', quarterLength=.5))

n7measure = stream.Measure()
n7measure.append(note.Note('E5', quarterLength=1.5))
n7measure.append(note.Note('B-5', quarterLength=.5))
n7measure.append(note.Note('D-6', quarterLength=2))
