#!/usr/bin/env python3

# Solutions to https://adventofcode.com/2020/day/1

from typing import Tuple, Sequence


def find_adding(x: Sequence[int], total=2020) -> Tuple[int, int]:
    '''
    Return the two entries from `x` that add up to `total`.
    `x` needs to be sorted in ascending order.
    '''
    x_desc = reversed(x)
    x_iter = iter(x)
    second = next(x_iter)
    for first in x_desc:
        while first + second <= total:
            if (first + second == total) and (first != second):
                return first, second
            try:
                second = next(x_iter)
            except StopIteration:
                return None, None
    return None, None


input_raw = open('day01_input.txt')
entries = (int(_.strip()) for _ in input_raw)
entries_asc = sorted(entries)
first, second = find_adding(entries_asc)
answer1 = first*second
print(f"The answer to the first puzzle is {answer1}")


def find_adding_three(x: Sequence[int], total=2020) -> Tuple[int, int, int]:
    '''
    Return the three entries from `x` that add up to `total`.
    `x` needs to be sorted in ascending order.
    '''
    for first in x:
        remainder = 2020 - first
        x_wo_first = [_ for _ in x if _ != first]
        second, third = find_adding(x_wo_first, remainder)
        if second is not None:
            return first, second, third


first, second, third = find_adding_three(entries_asc)
answer2 = first*second*third
print(f"The answer to the second puzzle is {answer2}")
