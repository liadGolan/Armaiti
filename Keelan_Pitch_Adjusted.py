#!/usr/bin/python3


from music21 import *
from helpers.part_corrector import part_corrector
from helpers.chord_sheet_keelan import *
from helpers.melody_sheet_keelan import *
from helpers.MelodyAdjustorKeelan import *


class Harmony:
    def __init__(self, start, steps):
        self.one_chord = chord.Chord(chord_sheet['one'], quarterLength=2)
        self.two_chord = chord.Chord(chord_sheet['two'], quarterLength=2)
        self.three_chord = chord.Chord(chord_sheet['three'], quarterLength=2)
        self.four_chord = chord.Chord(chord_sheet['four'], quarterLength=2)
        self.five_chord = chord.Chord(chord_sheet['five'], quarterLength=2)
        self.six_chord = chord.Chord(chord_sheet['six'], quarterLength=2)
        self.seven_chord = chord.Chord(chord_sheet['seven'], quarterLength=2)

        self.one_chords = []
        self.two_chords = []
        self.three_chords = []
        self.four_chords = []
        self.five_chords = []
        self.six_chords = []
        self.seven_chords = []
        self.pos = 0

        self.master_array = [start]

        self.rules = chord_rules

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

class FractalPart:
    def __init__(self, start, steps):
        self.n1_measure = self.create_n1_measure()
        self.n2_measure = self.create_n2_measure()
        self.n3_measure = self.create_n3_measure()
        self.n4_measure = self.create_n4_measure()
        self.n5_measure = self.create_n5_measure()
        self.n6_measure = self.create_n6_measure()
        self.n7_measure = self.create_n7_measure()

        self.n1_measures = []
        self.n2_measures = []
        self.n3_measures = []
        self.n4_measures = []
        self.n5_measures = []
        self.n6_measures = []
        self.n7_measures = []
        self.pos = 0

        self.rules = {
            'C': self.n1_measure,
            'D': self.n2_measure,
            'E': self.n3_measure,
            'F': self.n4_measure,
            'G': self.n5_measure,
            'A': self.n6_measure,
            'B': self.n7_measure
        }

        self.rulesBeforeFinal = rules_before_final

        self.master_array = [start]

        while steps > 1:
            self.master_array = self.fractal_step(self.master_array)
            steps -= 1

        self.ultra_stream = stream.Part()

    @staticmethod
    def create_n1_measure():
        return n1measure

    @staticmethod
    def create_n2_measure():
        return n2measure

    @staticmethod
    def create_n3_measure():
        return n3measure

    @staticmethod
    def create_n4_measure():
        return n4measure

    @staticmethod
    def create_n5_measure():
        return n5measure

    @staticmethod
    def create_n6_measure():
        return n6measure

    @staticmethod
    def create_n7_measure():
        return n7measure

    def fractal_step(self, old_array):
        master_array = []
        for n in old_array:
            to_be_added = self.rulesBeforeFinal[n]
            for e in to_be_added:
                master_array.append(e)
        return master_array

    def get_final_version(self, old_array):
        master_array = []
        for n in old_array:
            to_be_added = rules_before_final_for_generation[n]
            for e in to_be_added:
                master_array.append(e)
        return master_array

    def get_final_build(self):
        for e in self.master_array:
            if e is 'C':
                self.n1_measures.append(self.pos)
            elif e is 'D':
                self.n2_measures.append(self.pos)
            elif e is 'E':
                self.n3_measures.append(self.pos)
            elif e is 'F':
                self.n4_measures.append(self.pos)
            elif e is 'G':
                self.n5_measures.append(self.pos)
            elif e is 'A':
                self.n6_measures.append(self.pos)
            elif e is 'B':
                self.n7_measures.append(self.pos)
            else:
                print(e + 'ERROR')

            self.pos += 4

        self.ultra_stream.repeatInsert(self.n1_measure, self.n1_measures)
        self.ultra_stream.repeatInsert(self.n2_measure, self.n2_measures)
        self.ultra_stream.repeatInsert(self.n3_measure, self.n3_measures)
        self.ultra_stream.repeatInsert(self.n4_measure, self.n4_measures)
        self.ultra_stream.repeatInsert(self.n5_measure, self.n5_measures)
        self.ultra_stream.repeatInsert(self.n6_measure, self.n6_measures)
        self.ultra_stream.repeatInsert(self.n7_measure, self.n7_measures)

        return self.ultra_stream

def main():
    first = FractalPart('C', 4)
    part1 = first.get_final_build()
    part1.id = 'part1'
    second = Harmony('one', 4)
    part2 = second.get_final_build()
    part2.id = 'part2'
    adjustedMelody = melody_adjustor(second.master_array,first.get_final_version(first.master_array))
    part1, part2 = part_corrector(adjustedMelody, part2, first, second)
    score = stream.Score()
    score.insert(0, part1)
    score.insert(0, part2)
    score.show()


if __name__ == '__main__':
    main()
