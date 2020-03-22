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

    return tuple(new_card)


def find_sets(k, v, board):
    found = []

    # Make a hashmap version of board for quicker searching
    hash_board = {card: None for card in board}

    # For each set of v-1 cards, find what card (if any) would make a valid set
    almost_sets = list(itertools.combinations(board, v - 1))

    # For each almost_set, see if we have that card
    for a in almost_sets:
        last = last_card(k, v, a)
        if last is None:
            continue
        if last in hash_board:
            found.append(a + (last))

    return found


if __name__ == "__main__":

    k = 4
    v = 3

    board = random_board(k, v, 12)
    # board = [(1, 3, 3), (2, 2, 2), (3, 0, 1)]

    print(board)
    # print(last_card(k, v, board))
    print(find_sets(k, v, board))
