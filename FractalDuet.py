#!/usr/bin/python3


from music21 import *


class FractalPart:
    def __init__(self, start, steps):
        self.c_measure = self.create_c_measure()
        self.d_measure = self.create_d_measure()
        self.e_measure = self.create_e_measure()
        self.f_measure = self.create_f_measure()
        self.g_measure = self.create_g_measure()
        self.a_measure = self.create_a_measure()
        self.b_measure = self.create_b_measure()

        self.c_measures = []
        self.d_measures = []
        self.e_measures = []
        self.f_measures = []
        self.g_measures = []
        self.a_measures = []
        self.b_measures = []
        self.pos = 0

        self.rules = {
            'C': self.c_measure,
            'D': self.d_measure,
            'E': self.e_measure,
            'F': self.f_measure,
            'G': self.g_measure,
            'A': self.a_measure,
            'B': self.b_measure
        }

        self.rulesBeforeFinal = {
            'C': ('G', 'F', 'E', 'D'),
            'D': ('G', 'A', 'B', 'C'),
            'E': ('F', 'C', 'B', 'A', 'G'),
            'F': ('D', 'G', 'A', 'B', 'C'),
            'G': ('C', 'D', 'E', 'F', 'C'),
            'A': ('E', 'A'),
            'B': ('G', 'C'),
        }

        self.master_array = [start]

        while steps > 1:
            self.master_array = self.fractal_step(self.master_array)
            steps -= 1

        self.ultra_stream = stream.Part()

    @staticmethod
    def create_c_measure():
        measure = stream.Measure()
        measure.append(note.Note('G5', quarterLength=1))
        measure.append(note.Note('F5', quarterLength=1))
        measure.append(note.Note('E-5', quarterLength=1))
        measure.append(note.Note('D5', quarterLength=1))
        return measure

    @staticmethod
    def create_d_measure():
        measure = stream.Measure()
        measure.append(note.Note('G5', quarterLength=1))
        measure.append(note.Note('A5', quarterLength=1))
        measure.append(note.Note('B-5', quarterLength=1))
        measure.append(note.Note('C6', quarterLength=1))
        return measure

    @staticmethod
    def create_e_measure():
        measure = stream.Measure()
        measure.append(note.Note('F5', quarterLength=2))
        measure.append(note.Note('C6', quarterLength=.5))
        measure.append(note.Note('B-5', quarterLength=.5))
        measure.append(note.Note('A5', quarterLength=.5))
        measure.append(note.Note('G5', quarterLength=.5))
        return measure

    @staticmethod
    def create_f_measure():
        measure = stream.Measure()
        measure.append(note.Note('D6', quarterLength=2))
        measure.append(note.Note('G5', quarterLength=.5))
        measure.append(note.Note('A5', quarterLength=.5))
        measure.append(note.Note('B-5', quarterLength=.5))
        measure.append(note.Note('C6', quarterLength=.5))
        return measure

    @staticmethod
    def create_g_measure():
        measure = stream.Measure()
        measure.append(note.Note('C5', quarterLength=.5))
        measure.append(note.Note('D5', quarterLength=.5))
        measure.append(note.Note('E-5', quarterLength=.5))
        measure.append(note.Note('F5', quarterLength=.5))
        measure.append(note.Note('C6', quarterLength=2))
        return measure

    @staticmethod
    def create_a_measure():
        measure = stream.Measure()
        measure.append(note.Note('E-5', quarterLength=2))
        measure.append(note.Note('A5', quarterLength=2))
        return measure

    @staticmethod
    def create_b_measure():
        measure = stream.Measure()
        measure.append(note.Note('G5', quarterLength=2))
        measure.append(note.Note('C5', quarterLength=2))
        return measure

    def fractal_step(self, old_array):
        master_array = []
        for n in old_array:
            to_be_added = self.rulesBeforeFinal[n]
            for e in to_be_added:
                master_array.append(e)
        return master_array

    def get_final_build(self):
        for e in self.master_array:
            if e is 'C':
                self.c_measures.append(self.pos)
            elif e is 'D':
                self.d_measures.append(self.pos)
            elif e is 'E':
                self.e_measures.append(self.pos)
            elif e is 'F':
                self.f_measures.append(self.pos)
            elif e is 'G':
                self.g_measures.append(self.pos)
            elif e is 'A':
                self.a_measures.append(self.pos)
            elif e is 'B':
                self.b_measures.append(self.pos)
            else:
                print(e + 'ERROR')

            self.pos += 4

        self.ultra_stream.repeatInsert(self.c_measure, self.c_measures)
        self.ultra_stream.repeatInsert(self.d_measure, self.d_measures)
        self.ultra_stream.repeatInsert(self.e_measure, self.e_measures)
        self.ultra_stream.repeatInsert(self.f_measure, self.f_measures)
        self.ultra_stream.repeatInsert(self.g_measure, self.g_measures)
        self.ultra_stream.repeatInsert(self.a_measure, self.a_measures)
        self.ultra_stream.repeatInsert(self.b_measure, self.b_measures)

        return self.ultra_stream


def part_corrector(part1, part2, first, second):
    if first.pos > second.pos:
        rest_measures_needed = (first.pos - second.pos) / 4
        print(rest_measures_needed)
        rest_positions = []
        while rest_measures_needed > 0:
            rest_positions.append(second.pos)
            second.pos += 4
            rest_measures_needed -= 1
        rest_measure = stream.Measure()
        rest_measure.append(note.Rest(quarterLength=4))
        part2.repeatInsert(rest_measure, rest_positions)
        return part1, part2
    elif first.pos < second.pos:
        rest_measures_needed = (second.pos - first.pos) / 4
        print(rest_measures_needed)
        rest_positions = []
        while rest_measures_needed > 0:
            rest_positions.append(first.pos)
            first.pos += 4
            rest_measures_needed -= 1
        rest_measure = stream.Measure()
        rest_measure.append(note.Rest(quarterLength=4))
        part1.repeatInsert(rest_measure, rest_positions)
        return part1, part2
    else:
        return part1, part2


def main():
    first = FractalPart('C', 4)
    part1 = first.get_final_build()
    part1.id = 'part1'
    second = FractalPart('F', 4)
    part2 = second.get_final_build()
    part2.id = 'part2'
    part1, part2 = part_corrector(part1, part2, first, second)
    score = stream.Score()
    score.insert(0, part1)
    score.insert(0, part2)
    score.show()


if __name__ == '__main__':
    main()
