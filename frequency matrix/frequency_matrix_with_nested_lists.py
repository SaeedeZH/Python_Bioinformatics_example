# some declarations/ways for nested list (list of lists or matrix):
num = 4
# 1: regular
nes_ls = []
for i in range(num):
    nes_ls.append([])
print(nes_ls)

# 2: using comperhension
nes_ls = [[] for i in range(num)]
print(nes_ls)

# 3: using numpy
import numpy as np
nes_ls = np.empty((num,0)).tolist()  # because of 0, .tolist() is mandatory
print(nes_ls)
 
# or
nes_ls = np.zeros((num, 3))
print(nes_ls)
##############################################################
# nested list

def freq_list_by_matrix_v1(dna_list):
    # create empty freq matriix
    # i = 0,1,2,3 corespods to A, T, G, C
    freq_matrix = [[0 for j in range(len(dna_list[0]))] for i in "ACTG"]

    for dna in dna_list:
        for index, base in enumerate(dna):
             if base =="A": freq_matrix[0][index] +=1
             elif base =="T": freq_matrix[1][index] +=1
             elif base =="G": freq_matrix[2][index] +=1
             elif base =="C": freq_matrix[3][index] +=1
    return freq_matrix
                
dna_list = ['GGTAG', 'GGTAC', 'GGTGC']
print(freq_list_by_matrix_v1(dna_list))

# using dictionary for more convenient indexing

# The series of if tests in the Python function freq_list_of_lists_v1 are somewhat cumbersome,
# especially if we want to extend the code to other bioinformatics problems where the alphabet is larger.
# What we want is a mapping from base, which is a character, to the corresponding index 0, 1, 2, or 3. A Python dictionary 
# may represent such mappings:

def freq_list_by_matrix_v2(dna_list):
    base2index = {"A":0, "T":1, "G":2, "C":3}

    freq_matrix = [[0 for j in range(len(dna_list[0]))] for i in "ATCG"]
    for dna in dna_list:
        for index, base in enumerate(dna):
            freq_matrix[base2index[base]][index] += 1

    return freq_matrix
    
dna_list = ['GGTAG', 'GGTAC', 'GGTGC']
print(freq_list_by_matrix_v2(dna_list))

# using Numerical Python Array

# As long as each sublist in a list of lists has the same length, a list of lists can be replaced by a Numerical Python (numpy)
# array. Processing of such arrays is often much more efficient than processing of the nested list data structure.
# To initialize a two-dimensional numpy array we need to know its size, here 4 times len(dna_list[0]). 
import numpy as np
def freq_list_by_matrix_v3(dna_list):

    freq_matrix = np.zeros((4, len(dna_list[0])), dtype=np.int32)
    base2index = {"A": 0, "T":1, "G":2, "C":3}

    for dna in dna_list:
        for index , base in enumerate(dna):
            freq_matrix[base2index[base]][index] += 1

    #print(freq_matrix[base2index["A"]])
    return freq_matrix
    
dna_list = ['GGTAG', 'GGTAC', 'GGTGC']
print(freq_list_by_matrix_v3(dna_list))


# using Dictionary of Lists

# Instead of going from a character to an integer index via base2index, we may prefer to index frequency_matrix by the base name
# and the position index directly, like in ['C'][14]. This is the most natural syntax for a user of the frequency matrix. 
# The relevant Python data structure is then a dictionary of lists. That is, frequency_matrix is a dictionary
# with keys 'A', 'C', 'G', and 'T'. The value for each key is a list. Let us now also extend the flexibility such that
# dna_list can have DNA strings of different lengths. The lists in frequency_list will have lengths equal to the longest 
# DNA string. A relevant function is

def freq_list_by_matrix_v4(dna_list):
    n = max([len(dna) for dna in dna_list])  # Tip2: == max(len(dna) for dna in dna_list) or max(dna_list, key=len)
    freq_dic = { "A": [0]*n, "T": [0]*n, "C": [0]*n, "G": [0]*n} # Tip 1: ==  freq_dic ={base: [0]*n for base in ACTG"}

    for dna in dna_list:
        for index, base in enumerate(dna):
            freq_dic[base][index] += 1
    return freq_dic

dna_list = ['GGTAG', 'GGTAC', 'GGTGC']
#print(freq_list_by_matrix_v3(dna_list))

import pprint
pprint.pprint(freq_list_by_matrix_v4(dna_list))
# {'A': [0, 0, 0, 2, 0],
#  'C': [0, 0, 0, 0, 2],
#  'G': [3, 3, 0, 1, 1],
#  'T': [0, 0, 3, 0, 0]}

# Tip1: The initialization of frequency_matrix in the above code can be made more compact by using a dictionary comprehension:
# dict = {key: value for key in some_sequence}

# Tip2: n = max([len(dna) for dna in dna_list])
# for very long lists it is possible to avoid the memory demands of storing the result of the list comprehension,
# i.e., the list of lengths. Instead max can work with the lengths as they are computed:
 # n = max(len(dna) for dna in dna_list) === Generatore Comperhention!!!!

# unsing dictionary of dictionary

def freq_list_by_matrix_v5(dna_list):
    n = max([len(dna) for dna in dna_list])
    frequency_matrix = {base: {index: 0 for index in range(n)}
                        for base in 'ACGT'}
    for dna in dna_list:
        for index, base in enumerate(dna):
            frequency_matrix[base][index] += 1

    return frequency_matrix

dna_list = ['GGTAG', 'GGTAC', 'GGTGC']
# print(freq_list_by_matrix_v3(dna_list))

import pprint
pprint.pprint(freq_list_by_matrix_v5(dna_list))
# The output:
# {'A': {0: 0, 1: 0, 2: 0, 3: 2, 4: 0},
#  'C': {0: 0, 1: 0, 2: 0, 3: 0, 4: 2},
#  'G': {0: 3, 1: 3, 2: 0, 3: 1, 4: 1},
#  'T': {0: 0, 1: 0, 2: 3, 3: 0, 4: 0}}

# Tip: dictionary comperhention
# d = {key: value for key in sequence}
# is then constructed as
# d = dict([(key, value) for key in sequence])


# Using Arrays and Vectorization

# The frequency_matrix dict of lists for can easily be changed to a dict of numpy arrays: 
# just replace the initialization [0]*n by np.zeros(n, dtype=np.int). The indexing remains the same:

def freq_dict_of_arrays_v1(dna_list):
    n = max(dna_list, key=len)
    freq_matrix = {base : np.zeros(n, dtype=np.int16) for base in "ACTG"}

    for dna in dna_list:
        for index, base in enumerate(dna):
            freq_matrix[base][index] += 1
    return freq_matrix

# Having frequency_matrix[base] as a numpy array instead of a list does not give any immediate advantage,
# as the storage and CPU time is about the same. The loop over the dna string and the associated indexing is what consumes
# all the CPU time. However, the numpy arrays provide a potential for increasing efficiency through vectorization, 
# i.e., replacing the element-wise operations on dna and frequency_matrix[base] by operations on the entire arrays at once.
# Let us to explore the possibilities of vectorization. 
# We first convert the string to a numpy array of characters:
dna = "ACAT"
dna = np.array(dna, dtype='c')
print(dna) # array(['A', 'C', 'A', 'T'], dtype='|S1')

comp = dna == "A"
print(comp)  # array([ True, False,  True, False], dtype=bool)
# By converting b to an integer array i we can update the frequency counts for all indices by adding i to frequency_matrix['A']:
new_type = np.asarray(comp, dtype=int)
comp  # array([1, 0, 1, 0])
# ==> freq_matrix['A'] = freq_matrix['A'] + comp

# This recipe can be repeated for all bases:
# for dna in dna_list:
#         dna = np.array(dna, dtype='c')
#         for base in 'ACGT':
#             comp = dna == base
#             i = np.asarray(comp, dtype=np.int)
#             freq_matrix[base] = freq_matrix[base] + i

# It turns out that we do not need to convert the boolean array b to an integer array i, because doing arithmetics
#  with b directly is possible: False is interpreted as 0 and True as 1 in arithmetic operations. 
# We can also use the += operator to update all elements of freq_matrix[base] directly, without first computing
# the sum of two arrays freq_matrix[base] + i and then assigning this result to freq_matrix[base]. 
# Collecting all these ideas in one function yields the code:

def freq_dict_of_arrays_v2(dna_list):
    n = max(dna_list, key=len)
    # print(n) # GGTAG
    freq_matrix = {base: np.zeros(len(n), dtype=np.int16) for base in "ACTG"}

    for dna in dna_list:
        vector_dna = np.array(dna)
        print(vector_dna)
        for base in "ACTG":
            res = vector_dna == base
            #print(res)
            freq_matrix[base] += res
    return freq_matrix

dna_list = ['GGTAG', 'GGTAC', 'GGTGC']
# print(freq_list_by_matrix_v3(dna_list))

import pprint
pprint.pprint(freq_dict_of_arrays_v2(dna_list))

# This vectorized function runs almost 10 times as fast as the (scalar) counterpart freq_list_of_arrays_v1!