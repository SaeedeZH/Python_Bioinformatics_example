

def complement(seq):
    compe = {"A":"T", "T":"A", "C":"G", "G":"C"}
    seq_comp = [compe[s] for s in seq]
    return "".join(seq_comp)

def reverse_complement(seq):
    comp_seq = complement(seq)
    return reverse(comp_seq)

def reverse(seq):
    return(seq[::-1])

print(reverse_complement("ACTGCAT"))