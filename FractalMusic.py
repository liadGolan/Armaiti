#!/usr/bin/python3


from music21 import *


class Harmony:
    def __init__(self, start, steps):
        self.one_chord = chord.Chord(['F2', 'F3', 'A3', 'C4'], quarterLength=2)
        self.two_chord = chord.Chord(['G2', 'G3', 'B-3', 'D4'], quarterLength=2)
        self.three_chord = chord.Chord(['A2', 'A3', 'C4', 'E4'], quarterLength=2)
        self.four_chord = chord.Chord(['B-2', 'B-3', 'D4', 'F4'], quarterLength=2)
        self.five_chord = chord.Chord(['C3', 'C4', 'E4', 'G4'], quarterLength=2)
        self.six_chord = chord.Chord(['D3', 'D4', 'F4', 'A4'], quarterLength=2)
        self.seven_chord = chord.Chord(['E3', 'E4', 'G4', 'B-4'], quarterLength=2)

        self.one_chords = []
        self.two_chords = []
        self.three_chords = []
        self.four_chords = []
        self.five_chords = []
        self.six_chords = []
        self.seven_chords = []
        self.pos = 0

        self.master_array = [start]

        self.rules = {
            'one': ('one', 'four', 'one', 'five'),
            'two': ('six', 'two', 'five', 'one'),
            'three': ('one', 'six', 'four', 'five'),
            'four': ('seven', 'four', 'two', 'five'),
            'five': ('six', 'four', 'five', 'one'),
            'six': ('one', 'three', 'four', 'five'),
            'seven': ('one', 'six', 'two', 'five'),
        }

        while steps > 0:
            self.master_array = self.fractal_step(self.master_array)
            steps -= 1

    def fractal_step(self, array):
        master_array = []
        for e in array:
            to_be_added = self.rules[e]
            for i in to_be_added:
                master_array.append(i)
        return master_array

    def get_final_build(self):
        for e in self.master_array:
            if e is 'one':
                self.one_chords.append(self.pos)
            elif e is 'two':
                self.two_chords.append(self.pos)
            elif e is 'three':
                self.three_chords.append(self.pos)
            elif e is 'four':
                self.four_chords.append(self.pos)
            elif e is 'five':
                self.five_chords.append(self.pos)
            elif e is 'six':
                self.six_chords.append(self.pos)
            elif e is 'seven':
                self.seven_chords.append(self.pos)
            else:
                print('ERROR')

            self.pos += 2

        stram = stream.Stream()
        stram.repeatInsert(self.one_chord, self.one_chords)
        stram.repeatInsert(self.two_chord, self.two_chords)
        stram.repeatInsert(self.three_chord, self.three_chords)
        stram.repeatInsert(self.four_chord, self.four_chords)
        stram.repeatInsert(self.five_chord, self.five_chords)
        stram.repeatInsert(self.six_chord, self.six_chords)
        stram.repeatInsert(self.seven_chord, self.seven_chords)
        return stram


def main():
    hamony = Harmony('one', 4)
    hamony_stream = hamony.get_final_build()
    hamony_stream.insert(0, tempo.MetronomeMark(number=150))
    hamony_stream.show()


if __name__ == '__main__':
    main()
