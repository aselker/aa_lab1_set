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


def last_card(k, v, cards):
    """
    Given v-1 cards, what last card (if any) would make a valid set?
    """

    assert len(cards) == v - 1

    new_card = [None for _ in range(k)]
    for i in range(k):
        values = set((card[i] for card in cards))
        if len(values) == 1:
            new_card[i] = cards[0][i]
        elif len(values) == v - 1:
            for j in range(v):
                if j not in values:
                    new_card[i] = j
                    break
        else:
            return None  # These cards can't form a valid set

    return new_card


if __name__ == "__main__":

    k = 4
    v = 3

    board = random_board(k, v, v - 1)
    print(board)
    print(last_card(k, v, board))
