#!/usr/bin/env python3

import sys
from read_input import read_input
from set_solver import find_sets


def convert_to_set(file_name=None, data_in=None, num_vars=None):
    """Function to convert a 3 dimensional mapping problem to a set problem.

    Args (two options):
    file_name : str name of file to open
    OR
    data_in : list of all current pairings in a 3d_mapping problem
    num_vars : The number of vars in the problem (NOTE: this is passed in in case an INVALID set of data is given)

    Output:
    list of all "cards" in set

    """
    # Big difference is to add a "v+1" card
    # What this does is compensate for beign able to have sets with an overlapping val if all are the same
    if file_name:
        (data, _, num_dims, num_vars, num_solns) = read_input(file)
        # print(data)
    else:
        data = data_in
        num_dims = len(data_in[0])
        # num_vars = 3 # TODO: erm... how are we calculating this I'll take it in for now?

    return (add_set_card(data, num_dims, num_vars), num_dims, num_vars + 1, num_solns)


def add_set_card(data, num_dims, num_vars):
    """Function that adds the additional card to the data to convert.

    Args:
    data : Data of a 3d mapping problem
    num_dims : int number of dimensions of the data
    num_vars : int the number of vars for a given element.

    Output:
    list with the augmented card

    """
    new_card = [num_vars] * num_dims
    data.append(tuple(new_card))
    return data


if __name__ == "__main__":
    files = sys.argv[1:]
    for file in files:
        print(f"File name: {file}")
        (set_out, num_dims, num_vars, num_solns) = convert_to_set(file)
        print(f"Converted to set format we get: {set_out}")
        output = find_sets(num_dims, num_vars, set_out)
        if output:
            print(f'Got {len(output)} sets as solutions; there are supposed to be {num_solns}')
            print(f'A final matched set is: {output[0][:-1]}')
            all_sets = [x[:-1] for x in output]
            print(f'All possible matched sets are: {all_sets}')
        else:
            print("No matchings found.")

        print("")  # Line break
