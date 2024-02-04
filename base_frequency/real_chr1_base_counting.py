from finding_base_frequencies import get_base_frequencies_final, get_base_count_v1, get_base_frequencies_v1

def read_dnafile_v1(file_name):
    dna = ''
    with open(file_name, 'r' ) as handler:
        dna = handler.read()
    return dna

def read_dnafile_v2(file_name):
    dna = ''
    handler = open(file_name, 'r')
    #print(type(handler))  # <class '_io.TextIOWrapper'>
    lines = handler.readlines()
    dna = ''.join(line.strip() for line in lines)
    return dna

def read_dnafile_v3(file_name):
    dna = ''
    for line in open(file_name, 'r'):
        dna += line.strip()
    return dna

def main():
    dna = read_dnafile_v2("./data/e_coli copy.txt")
    print(dna)
    print(get_base_frequencies_final(dna))
    print(get_base_count_v1(dna))
    print(get_base_frequencies_v1(dna))
if __name__ == "__main__":
    main()