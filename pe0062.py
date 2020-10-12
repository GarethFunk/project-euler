import numpy as np
from collections import OrderedDict


class Cube():
    def __init__(self, stop=None):
        self.i = 0
        self.stop = stop

    def __next__(self):
        self.i += 1
        if self.stop is not None and self.i > self.stop:
            raise StopIteration
        return self.i**3

    def __iter__(self):
        self.i = 0
        return self

    def next(self):
        return self.__next__()


def digitSet(n):
    digits = list(str(n))
    digit_dict = OrderedDict()
    for d in "0123456789":
        digit_dict.update([(d, digits.count(d))])
    return digit_dict


if __name__ == "__main__":
    # The naive way of working out all the digit permutations and checking them for cubeness is way too slow.
    # So, let's keep on generating cube numbers and use sets to find when we have 5 numbers with the same digits
    # actually we can't have sets because of repeated digits but you get the idea
    old_cubes = []
    for cube in Cube():
        cube = digitSet(cube)
        old_cubes.append(cube)  # Put it in the list now so we find ourself.
        digit_matches = []
        for i, old_cube in enumerate(old_cubes):
            if cube == old_cube:
                # We have a digit match
                digit_matches.append(i)
        if len(digit_matches) == 5:
            # We can recover the original cube numbers because the index in the list is the number that was cubed
            for i in digit_matches:
                print(i+1)
                print((i+1)**3)
            break
