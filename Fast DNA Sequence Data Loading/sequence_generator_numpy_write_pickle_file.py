import random, sys, pickle
import numpy as np


def main():
# This program is run via command line with 3 parameters includes: number of sequences, start of lengths, end of lenghts

    if not invalid_argument():
        print(sys.argv)
        seq_list = generate_dna_sequence(sys.argv)  # sys.argv is a list of strs includes name of program
        seq_np_list = convert_to_numpy_list(seq_list)
        write_to_pickle_file(seq_np_list)

def generate_dna_sequence(args):
    seq_num = int(args[1])
    seq_start_len = int(args[2])
    seq_end_len = int(args[3])

    seq_list = []
    for i in range(seq_num):
        dna = ""
        for l in range(random.randint(seq_start_len, seq_end_len)):
            dna += gen_dna(random.randint(0,3))
        seq_list.append(dna)
    return seq_list

def gen_dna(n):
    dna = {0:"A", 1:"C", 2:"T", 3:"G"}
    return dna[n]

def convert_to_numpy_list(seq_list):
    return np.array(seq_list)

def write_to_pickle_file(seq_list):

    try:

        with open("./data/sequence_list.pkl", "wb") as f:
            pickle.dump(seq_list, f)
            print("The seq list is writen to pickle file!")
    except Exception as er:
        print("There is an error in writing seq list to pickle file! {}".format(er))

def invalid_argument():
    if len(sys.argv) != 4:
       print("The number of parameters must be four!")
       return True
    
    try:
        int(sys.argv[1])
        int(sys.argv[2])
        int(sys.argv[3])
    except TypeError as er:
        print(er)
        return True
    
    return False

if __name__ == "__main__":
    main()