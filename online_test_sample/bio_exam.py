def reverse_complement2(seq: str):
    """This function gets a DNA seq and return its reverse complement.
    Args:
        seq (str): A string representing the DNA sequence.
    Returns:
        str: A string representing reverse complement of input str
    """
    reverse_dic = {"A":"T", "T":"A", "C":"G", "G":"C"}
    rev_str = ""
    for ch in seq:
        rev_str += reverse_dic[ch]
    return rev_str[::-1]
# or 
#  return("".join(reverse_dic[base] for base in reversed(seq)))

# Function 2: GC Content (5 minutes)
# This function takes a DNA sequence as input and calculates its GC content (percentage of G and C nucleotides).

def gc_content(seq):
    """This function takes a DNA sequence and calculates its GC content.
    Args:
        seq (str): A sring representing the DNA sequence.

    Returns:
        float: A float representing the GC content as a percentage.
    """
    #gc = [1 for ch in seq if ch=="G" or ch=="C"]
    gc = (seq.count("C") + seq.count("G")) / len(seq) * 100
    return gc
    #return sum(gc)/len(seq) * 100

# gc_per = gc_content("ACTCGCGC")
# print(f"The percentage of GC in seq is: {gc_per:.2f}%")

# Function 3: FASTA Parser (10 minutes)
# This function takes a FASTA file path as input and parses it, returning a dictionary where keys are sequence IDs and values are their corresponding sequences.

def parse_fasta(fasta_file):
    """This function parse a Fasta file and return a dictionary containing sequences.
    Args:
        fasta_file (file path): path to the Fasta file
    Returns:
        Dict : A dictionary where keys are IDs and values are their sequences.
    """
    fasta_dic = {}
    with open (fasta_file) as handler:
        for line in handler:
            if line.startswith(">"):
                seq_id = line.split(" ")[0][1:]
            else:
                fasta_dic[seq_id] = line
    return len(fasta_dic)

# print(f"Number of sequences: {len(parse_fasta("../data/sample1.fa"))}")

# Bonus Function (5 minutes)
# This function implements a simple algorithm to identify potential open reading frames (ORFs) in a DNA sequence.
def orfs(seq, start_codon="ATG", stop_codon=["TAA", "TAG", "TGA"]):
    """This function identifies potentioal open reading frames (ORFs) in a DNA sequence.

    Args:
        seq (str): A string representing DNA sequence.
        start_codon (str, optional): The start codon. Defaults to "ATG".
        stop_codon (list, optional): A list of stop codons. Defaults to ["TAA", "TAG", "TGA"].

    Returns:
        list: A list of tuples (start_index, end_index) representing potential ORFs.
    """
    codons = []
    #for i in range(len(seq)):
    while seq.find(start_codon) != -1:
        start = seq.find(start_codon)
        for stop in stop_codon:
            end = seq[start:].find(stop)
            if end != -1:
                codons.append((start, start+end))
        seq = seq[start + 1:]
    return codons

#print(orfs("ATGGGATGACCCCCTAAGGGGGTAGTTTTTTTGA"))
                
