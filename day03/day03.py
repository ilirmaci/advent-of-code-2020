#!/usr/bin/env python3

from typing import Sequence, Iterator
import math


def path(pattern: Sequence[str], vstep: int, hstep: int) -> Iterator[str]:
    '''
    Return iterator with values of all encountered squares.
    '''
    vindex = range(0, len(pattern), vstep)
    hindex = ((hstep * ii) % len(pattern[0]) for ii, _ in enumerate(vindex))
    return (pattern[rr][cc] for rr, cc in zip(vindex, hindex))


def num_trees(path: Iterator[str]) -> int:
    '''
    Return the count of trees in path.
    '''
    return sum(1 for _ in path if _ == '#')


input_raw = open('day03_input.txt')
pattern = [_.strip() for _ in input_raw]
answer1 = num_trees(path(pattern, 1, 3))
print(f"The answer to the first puzzle is {answer1}")

steps = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
paths = (path(pattern, vstep, hstep) for vstep, hstep in steps)
ntrees = [num_trees(_) for _ in paths]
answer2 = math.prod(ntrees)
print(f"The answer to the second puzzle is {answer2}")
