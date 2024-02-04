# From a coding perspective we may create a function for counting how many times A, C, G, and T appears in the string 
# and then another function for computing the frequencies. In both cases we want dictionaries such that we can index with
# the character and get the count or the frequency out. Counting is done by:

def get_base_count_v1(dna):
    counts = {"A":0, "C":0, "G":0, "T":0}
    for ch in "ACTG":
        counts[ch] = dna.count(ch)
    return counts

def get_base_count_v2(dna):
    counts = {"A":0, "C":0, "G":0, "T":0}
    for base in dna:
        counts[base] +=1
    return counts

def get_base_count_v3(dna):
    counts = {base: dna.count(base) for base in "ACTG"}      
    return counts

def get_base_frequencies_v1(dna):
    counts = get_base_count_v1(dna)
    return({base: round(counts[base]/len(dna), 3) for base in "ACTG"})

def get_base_frequencies_v2(dna):
    counts = get_base_count_v1(dna)
    return({base: (freq*0.1)/len(dna) for base,freq in counts.items()})

## Since we learned at the end of the section Efficiency Assessment that dna.count(base) was much faster than 
# the various manual implementations of counting, we can write a faster and simpler function for computing all 
# the base frequencies:
### In one function with better performance: ###

def get_base_frequencies_final(dna):
    return({base: (dna.count(base)*1.0)/len(dna) for base in "ATCG"})

def format_frequencies(frequencies):
    return ','.join ( [f"{base} with {freq :.3f} frequencies" for base, freq in frequencies.items()])


def main():
    dna = "ATGCTGCTA"
    print(get_base_count_v3(dna))
    print(get_base_frequencies_v2(dna))
    print(get_base_frequencies_final(dna))
    frequencies = get_base_frequencies_final(dna)
    print(type(frequencies))
    print(format_frequencies(frequencies))

if __name__ == "__main__":
    main()