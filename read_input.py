import random


def read_input(file):
    # Step 1: Read input
    # Using readlines()
    file1 = open(file, 'r')
    lines = file1.readlines()

    count = 0
    # Strips the newline character
    cleaned_input = []
    num_dims = None
    num_vars = None
    for line in lines:
        stripped = line.strip()
        if stripped[0] == "c":
            pass
        elif stripped[0] == "p":
            split = stripped.split()
            num_dims = int(split[1])
            num_vars = int(split[2])
        else:
            cleaned_input.append(tuple([int(x) for x in stripped.split()]))

    num_cards = len(cleaned_input)
    print(f'input read in is: {cleaned_input}')
    print(f'num_vars is: {num_vars}')
    print(f'num_dims is: {num_dims}')
    return (cleaned_input, num_cards, num_dims, num_vars)



if __name__ == "__main__":
    files = ["3d_mappingtest.txt"]
    for file in files:
        print(f'File name: {file}')
        set_out = read_input(file)
        print(set_out)
