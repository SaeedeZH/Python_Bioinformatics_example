from pprint import pprint
import numpy as np

# Dot plots are commonly used to visualize the similarity between two protein or nucleic acid sequences.
# They compare two sequences, say d1 and d2, by organizing d1 along the x-axis and d2 along the y-axis of a plot.
# When d1[i] == d2[j] we mark this by drawing a dot at location i,j in the plot.

# Using Lists of Lists
def dot_plot_for_two_dna(dna_x, dna_y):
    # create dotplot_matrix by using list of lists
    dotplot_matrix = [ [0 for y in dna_y] for x in dna_x]

    for index1, base1 in enumerate(dna_x):
        for index2, base2 in enumerate(dna_y):
            if base1 == base2:
                dotplot_matrix[index1][index2] = 1

    return dotplot_matrix

# One can, alternatively, translate the list of lists to a multi-line string containing the whole plot as a string object.
# This implies joining all the characters in each row and then joining all the rows:

def make_string_expanded(dotplot_matrix):
    # concat the dotplot matrix as a string to show
    rows = [''.join(row) for row in dotplot_matrix] # or:
    # rows = []
    # for row in M2:
    #     r =''.join(row)
    #     rows.append(r)
    plot = '\n'.join(rows)
    return plot

def dotplot_numpy(dna_x, dna_y):
    # create dotplot_matrix by using numpy
    dotplot_matrix = np.zeros((len(dna_x), len(dna_y)), dtype=np.int_)
    
    for index1, base1 in enumerate(dna_x):
        for index2, base2 in enumerate(dna_y):
            if base1 == base2:
                dotplot_matrix[index1, index2] = 1
    return dotplot_matrix

def main():
    dna_x = 'TAATGCCTGAAT'
    dna_y = 'CTCTATGCC'
    pprint(dot_plot_for_two_dna(dna_x, dna_y))

    M2 = [['1', '1', '0', '1'],
            ['1', '1', '1', '1'],
            ['0', '0', '1', '0'],
            ['0', '0', '0', '1']]
    
    print(make_string_expanded(M2))

    print(dotplot_numpy(dna_x, dna_y))


if __name__== "__main__":
    main()