#!/usr/bin/python3


import music21


class Harmony:
    def __init__(self, start, steps):
        self.one_chord = music21.chord.Chord(['F2', 'F3', 'A3', 'C4'], quarterLength=2)
        self.two_chord = music21.chord.Chord(['G2', 'G3', 'B-3', 'D4'], quarterLength=2)
        self.three_chord = music21.chord.Chord(['A2', 'A3', 'C4', 'E4'], quarterLength=2)
        self.four_chord = music21.chord.Chord(['B-2', 'B-3', 'D4', 'F4'], quarterLength=2)
        self.five_chord = music21.chord.Chord(['C3', 'C4', 'E4', 'G4'], quarterLength=2)
        self.six_chord = music21.chord.Chord(['D3', 'D4', 'F4', 'A4'], quarterLength=2)
        self.seven_chord = music21.chord.Chord(['E3', 'E4', 'G4', 'B-4'], quarterLength=2)

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

        stream = music21.stream.Stream()
        stream.repeatInsert(self.one_chord, self.one_chords)
        stream.repeatInsert(self.two_chord, self.two_chords)
        stream.repeatInsert(self.three_chord, self.three_chords)
        stream.repeatInsert(self.four_chord, self.four_chords)
        stream.repeatInsert(self.five_chord, self.five_chords)
        stream.repeatInsert(self.six_chord, self.six_chords)
        stream.repeatInsert(self.seven_chord, self.seven_chords)
        return stream


def main():
    harmony = Harmony('one', 3)
    harmony_stream = harmony.get_final_build()
    harmony_stream.insert(0, music21.tempo.MetronomeMark(number=150))
    harmony_stream.show()


if __name__ == '__main__':
    main()
