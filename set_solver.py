#!/usr/bin/env python3

import itertools
import random

"""
A solver for the card game Set, that finds all valid sets.  Works with
arbitrary numbers of properties and values.

Cards are represented as tuples of k values, each from 0 to v-1, where k is the
number of properties, and v the number of values.  In a normal game, k=4
(shape, color, number, infigg) and v=3 (oval, diamond, squiggle; solid, lines,
empty; etc.).  A set is a list of cards.
"""


def random_board(k, v, n):
    """
    Generate a random Set board with k=k, v=v, and n cards.
    """
    deck = list(itertools.product(*[list(range(v)) for _ in range(k)]))
    return random.sample(deck, n)


if __name__ == "__main__":
    print(random_board(4, 3, 12))
