#!/usr/bin/python3

from music21 import *
from helpers.chord_sheet import *
from helpers.melody_sheet import *

def melody_adjustor(harmony, melody):
    chord_iterator = 0;
    ultra_stream = stream.Part()

    current_measure = stream.Measure()
    beats_left_in_measure = 4
    for measure in melody:
        current_chord = harmony[chord_iterator]
        current_root = get_current_root(current_chord) - 1

        for cnote in measure:
            current_note = ''
            for key,value in soc.items():
                if value is cnote[0]:
                    current_note = key
            new_number = int(current_note[1]) + current_root
            if new_number > 7:
                new_number = new_number - 7
            new_note_key = 'n' + str(new_number)
            new_octave = cnote[2] + get_current_octave_adjuster(cnote[0], soc[new_note_key])
            full_pitch = soc_in_key[new_note_key] + str(new_octave)
            current_length = cnote[1]
            current_measure.append(note.Note(full_pitch, quarterLength=current_length))
            beats_left_in_measure = beats_left_in_measure - cnote[1]
        
        if beats_left_in_measure == 0.0:
            ultra_stream.append(current_measure)
            beats_left_in_measure = 4
            current_measure = stream.Measure()
        chord_iterator = chord_iterator + 1
    
    return ultra_stream


def get_current_root(currnet_chord):
    if currnet_chord is 'one':
        return 1
    elif currnet_chord is 'two':
        return 2
    elif currnet_chord is 'three':
        return 3
    elif currnet_chord is 'four':
        return 4
    elif currnet_chord is 'five':
        return 5
    elif currnet_chord is 'six':
        return 6
    elif currnet_chord is 'seven':
        return 7
    else:
        print("ERROR")

def get_current_octave_adjuster(old_pitch, new_pitch):
    if old_pitch is 'C':
        return 0
    elif old_pitch is 'D':
        if new_pitch is 'C':
            return 1
        else:
            return 0
    elif old_pitch is 'E':
        if new_pitch is 'C':
            return 1
        elif new_pitch is 'D':
            return 1
        else:
            return 0
    elif old_pitch is 'F':
        if new_pitch is 'C':
            return 1
        elif new_pitch is 'D':
            return 1
        elif new_pitch is 'E':
            return 1
        else:
            return 0
    elif old_pitch is 'G':
        if new_pitch is 'C':
            return 1
        elif new_pitch is 'D':
            return 1
        elif new_pitch is 'E':
            return 1
        elif new_pitch is 'F':
            return 1
        else:
            return 0
    elif old_pitch is 'A':
        if new_pitch is 'B':
            return 0
        else:
            return 1
    elif old_pitch is 'B':
        return 1
    else:
        print("ERROR")
