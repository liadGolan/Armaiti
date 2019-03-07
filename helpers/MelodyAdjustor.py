#!/usr/bin/python3

from music21 import *
from helpers.chord_sheet import *

def melody_adjustor(harmony, melody_stream):
    basis = harmony.master_array
    return melody_stream.flat.elements[0].fullName
