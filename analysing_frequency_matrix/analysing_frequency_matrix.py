
import pprint

# ex. [[2, 0, 2]
#     [1, 2, 0]
#     [0, 1, 0]
#     [0, 0, 1]]
# We see that for position 0, which corresponds to the left-most column in the table, the symbol A has the highest frequency
# (2). The maximum frequencies for the other positions are seen to be C for position 1, and A for position 2.
# The consensus string is therefore ACA. Note that the consensus string does not need to be equal to any of the substrings 
# that formed the basis of the frequency matrix (this is indeed the case for the above example).

# List of Lists of Frequency Matrix

def consensus_string_for_most_frequent_base_v1(freq_matrix):

    index2base = {0:'A', 1:'C', 2:'G', 3:'T'}
    consensus_str = ''
   
    for p in range(len(freq_matrix[0])):
        max_base = -1
        position = -1
        for b in range(len(freq_matrix)):
            if freq_matrix[b][p] > max_base:
                max_base = freq_matrix[b][p]
                position = b
        consensus_str += index2base[position]

    return consensus_str
     
# Since this code requires frequency_matrix to be a list of lists we should insert a test and raise 
# an exception if the type is wrong:

# This code should add the begining if the main function
def  consensus_string_for_most_frequent_base1_v2(freq_matrix):
    if isinstance(freq_matrix, list) and isinstance(freq_matrix[0], list):
        pass # right type
    else: 
        raise TypeError("frequency matrix must be List of List!")
    ...

# consensus_string_for_most_frequent_base1_v1(freq_matrix)
    
# Dict of Dicts Frequency Matrix
def consensus_string_for_most_frequent_base_v3(freq_matrix_dic):
    # Input parameter checknig
    if isinstance(freq_matrix_dic, dict) and isinstance(freq_matrix_dic["A"], dict):
        pass # right input
    else:
        raise TypeError('frequency matrix must be Dict of Dict!')
    # The main algorithm
    consensue_str = ''
    for v in range(len(freq_matrix_dic["A"])):
        max_freq = -1
        position = None
        for key, value in freq_matrix_dic.items():
            if value[v] > max_freq:
                max_freq = value[v]
                position = key
        consensue_str += position

    return consensue_str
        
def main():
    ## list of lists
    dna_list = ["ACT", "CCA", "AGA"]
    freq_matrix = [[2, 0, 2],
                [1, 2, 0],
                [0, 1, 0],
                [0, 0, 1]]
    
    pprint.pprint(freq_matrix)
    print(consensus_string_for_most_frequent_base_v1(freq_matrix))
   

    # Dict of Dicts
    dna_list = ["ACT", "CCA", "AGA"]
    freq_matrix_dic = { "A": {0:2, 1:0, 2:1},
                "C": {0:1, 1:0, 2:0},
                "G": {0:0, 1:1, 2:0},
                "T": {0:1, 1:0, 2:2}}
    
    pprint.pprint(freq_matrix_dic)
    print(consensus_string_for_most_frequent_base_v3(freq_matrix_dic))

if __name__ == "__main__":
    main()