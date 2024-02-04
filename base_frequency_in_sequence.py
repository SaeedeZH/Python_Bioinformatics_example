import time
import random

def generate_string(n, alphabet="ACTG"):
    """ Generate a sequence with lenght n.

    Args:
        n (integer): lenght of sequence
        alphabet (string): the alphabet of sequences. Defaults to "ACTG".

        Returns:
        dna : generated sequence
    """    
    ls = [random.choice(alphabet) for i in range(n)]
    dna = "".join(ls)  # convert a list to string
    return(dna)


def count_base2(dna, base):
    """count the number of base in the dna sequence.

    Args:
        dna (string): an input sequence
        base (char): a base for counting 

    Returns:
        integer : frequency of the base
    """    
    ls = []
    for c in dna:
        ls.append( True if c == base else False )
    return sum(ls)


functions = [ count_base2(generate_string(100), "T"), count_base2(generate_string(1000), "T"), count_base2(generate_string(10000), "T")
             ,count_base2(generate_string(10000), "T"),count_base2(generate_string(10000000), "T")]
timing = []

t0 = time.time()
print(t0)
freq = functions[4]
t1 = time.time()
print(t1)
cpu_time = t1 - t0
#timing.append(("%.10f" % cpu_time, freq))
timing.append((cpu_time, freq))
print(timing)