#!/usr/bin/python3


from music21 import *


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

# def part_corrector_two(staffs, generators):
#     max = 0
#     for genrators as generator:
#
