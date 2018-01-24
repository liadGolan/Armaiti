#!/usr/bin/python3


from music21 import *


class FractalPart:
    def __init__(self):
        self.rules = {}

    @staticmethod
    def create_whole_measure():
        pass


def main():
    n = note.Note("A2", type='quarter')
    v = volume.Volume(velocity=127)
    n.volume = v

    drumPart = stream.Part()
    drumPart.insert(0, instrument.Woodblock())

    drumMeasure = stream.Measure()
    drumMeasure.append(n)
    drumPart.append(drumMeasure)

    drumPart.show()


if __name__ == '__main__':
    main()
