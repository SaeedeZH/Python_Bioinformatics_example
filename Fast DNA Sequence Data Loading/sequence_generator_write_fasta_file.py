import sys, random, textwrap

def main():
# This program is run via command line with 3 parameters includes: number of sequences, start of lengths, end of lenghts

    if not invalid_argument():
        dna_dict = gen_dna_sequence_fasta_format(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
        write_seq_to_file(dna_dict, "./data/output.fasta")

def gen_dna_sequence_fasta_format(seq_num, start_len, end_len):
    '''
    Generate seq_num sequences with lenght beetween start_len and end_len
    '''
    print(gen_dna_sequence_fasta_format.__doc__)
    seqs_dic = {}
    for i in range(seq_num):
        seq_str = ""
        for j in range(random.randint(start_len, end_len)):
            seq_str += gen_DNA(random.randint(0,3))
        seq_title = f">Sequence {i+1} of {seq_num}"
        seqs_dic[seq_title] = seq_str

    return seqs_dic

def gen_DNA(n):
    dna_dic = {0:"A", 1:"T", 2:"C", 3:"G"}
    return dna_dic[n]

def write_seq_to_file(seqs_dic, seq_file):
    #print(seqs_dic)
    with open(seq_file, "w") as handler:
        for k, v in seqs_dic.items():
            handler.write("\n")
            handler.write(k)
            handler.write("\n")
            handler.write("\n".join(textwrap.wrap(v, 80)))
            handler.write("\n")
    
def invalid_argument():
    try:
        if len(sys.argv) != 4:
            #print("invalid argument length! we need number of seqs, start length and end length")
            raise Exception("invalid argument length! we need number of seqs, start length and end length") # create one error
    except Exception as e:   # handle or error managment without Traceback!
        print(e)
        return True
    try:
        int(sys.argv[1])    # all input args are considered as the srings, but there are no problem with int args! 
        int(sys.argv[2])
        int(sys.argv[3])
    except Exception as er:
        print(f"Invalid argument type: <int> <int> <int> {er}")
        return True
    
    return False


if __name__ == "__main__":
    main()