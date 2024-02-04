# For example, if our set of DNA sequences are TAG, GGT, and GGG, the table of frequency matrix becomes:
# there are only four rows in the frequency matrix:
# base: 0 1 2
# A	    0 1 0
# C	    0 0 0
# G	    2 2 2
# T	    1 0 1

# In the following we shall present different data structures to hold such a table and 
# different ways of computing them. The table is known as a frequency matrix in bioinformatics. 

# method 1: Separate Frequency Lists
# Since we know that there are only four rows in the frequency matrix, 
# an obvious data structure would be four lists, each holding a row. A function computing these lists may look like:

def freq_matrix(dna_list):
    ln_dna = len(dna_list[0])
    A_lst = [0]*ln_dna
    C_lst = [0]*ln_dna
    G_lst = [0]*ln_dna
    T_lst = [0]*ln_dna

    for dna in dna_list:
        for base in enumerate(dna):
            if base[1] == "A": A_lst[base[0]]+=1
            elif base[1] == "C": C_lst[base[0]]+=1
            elif base[1] == "G": G_lst[base[0]]+=1
            elif base[1] == "T": T_lst[base[0]]+=1
    return A_lst, C_lst, G_lst, T_lst

#A_lst, C_lst, G_lst, T_lst = freq_matrix(["TAG", "GGT", "GGG"])
for i in [freq_matrix(["TAG", "GGT", "GGG"])]:
    print(f"The ferq for A, C, G, T are respectivly=", i)

# note: enumerate function, ex:
for index, base in enumerate("AGCTT"):
    print(index, base)