# Fast DNA Sequence Data Loading
# List vs NumPy Array

# The genomics DNA sequence data can be imported from many different sources, including files, databases, clouds, etc.
# To use this data for any statistical analysis, it needs to be loaded into any programming data object based on the selected language.
# In Python, the most common data structures are tuples, sets, dictionaries, and lists.
# From the Python Data Ecosystem libraries, the most useful ones are NumPy arrays.
# NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices,
# along with a large collection of high-level mathematical functions to operate on these arrays.

# Many times, this needed genomics data is huge, and it takes some time to load it into the selected programming data object.
# NumPy arrays are the fastest data manipulation structures in Python today. Here are three main reasons:
#   1- A NumPy array is a collection of similar data types that is densely packed in memory. 
#      A Python list can have different data types, which impose many extra constraints when performing computations on it.
#   2- NumPy is capable of dividing a task into multiple subtasks and processing them in parallel.
#   3- NumPy functions are implemented in C, which further enhances its speed compared to Python lists.
# In this paper, I would like to find out if this is true with thousands of rows in a genomics DNA sequence string dataset. 
# https://ernest-bonat.medium.com/machine-learning-applications-in-genomics-life-sciences-by-ernest-bonat-ph-d-83598e67ccbc

# Maybe List can be faster than NumPy array sometimes? In the paper Python Lists Are Sometimes Much Faster Than NumPy. 
# Here’s Proof are shown some examples when List are faster than NumPy array (when items must be append in the np array). 

# a simple DNA sequence generator: https://github.com/jacobtonder/DNASequenceGenerator/blob/master/main.py
# It’s important to mention that many Python Data Ecosystem libraries are built on top of NumPy like Pandas, SciPy, Matplotlib, etc.  

# Here is an example for loading sequences into list and np.array comparition:

from sequence_generator_numpy_write_pickle_file import generate_dna_sequence, convert_to_numpy_list, write_to_pickle_file
import numpy as np
import pickle
import time

def load_empty_list(seq_list):
    """
    load empty list with seq list args:
    seq_list (list): test dna sequence list
    returns: empty_list (list)
    """  
    try:
        empty_list = []
        for seq in seq_list:
            empty_list.append(seq)
    except Exception as err:
        print(err)
    return empty_list

# This function has less speed than the loading to list, just because of using np.append()!
def load_empty_nparray(seq_list):
    """
    load empty list with seq list args:
    seq_list (list): test dna sequence list
    returns: empty_nparray (list)
    """  
    try:
        nparray = []
        for seq in seq_list:
            nparray = np.append(nparray, seq)
    except Exception as err:
        print(err)
    return nparray

# This function has more speed than the loading to list, just because of not using np.append()!
def load_empty_nparray_1(seq_list):
    nparray_1 = np.array(seq_list)
    return nparray_1

def main():
    # generate 10000 seq in a pickle file
    seq_num = 100
    args = (0, seq_num, 150, 150)
    seq_list = generate_dna_sequence(args)
    seq_nparray = convert_to_numpy_list(seq_list)
    write_to_pickle_file(seq_nparray)

    # deserialize the numpy array pickle file to np array
    with open("./data/sequence_list.pkl", "rb") as f:
        seq_nparray = pickle.load(f)
    # covert np array to list
    seq_list = seq_nparray

    # using list for loading
    start_time = time.time()
    load_empty_list(seq_list)
    end_time = time.time()
    duration = end_time - start_time
    print("The time loading for {} seq from list to list is {}".format(seq_num, duration))

    # using np array for loading with help of .append()
    start_time = time.time()
    load_empty_nparray(seq_list)
    end_time = time.time()
    duration = end_time - start_time
    print("The time loading for {} seq from np array to list is {}".format(seq_num, duration))

    # using np array for loading without .append() that is faster
    start_time = time.time()
    load_empty_nparray_1(seq_list)
    end_time = time.time()
    duration = end_time - start_time
    print("The time loading for {} seq from np array to list is {}".format(seq_num, duration))

if __name__ == main():
    main()


