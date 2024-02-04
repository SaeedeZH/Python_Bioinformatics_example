# Efficiency Assessment, 
# different methods and implmentation for Counting letters/base/bases

import random
def generate_string(n, alphabet="ACTG"):
    ls = [random.choice(alphabet) for i in range(n)]
    dna = "".join(ls)  # convert a list to string
    return(dna)

#####################################################################

# first solution:
# List Iteration
def count_v1(dna, base):
    dna = list(dna)  # convert string to list of letters
    i = 0            # counter
    for c in dna:
        if c == base:
            i += 1
    return i

# String Iteration
# A slight improvement of our solution is therefore to iterate directly over the string:
def count_v2(dna, base):
    i = 0 # counter
    for c in dna:
        if c == base:
            i += 1
    return i


# Inserting print statements and examining the variables is the simplest approach to investigating what is going on:
def count_v2_demo(dna, base):
    print ('dna:', dna)
    print ('base:', base)
    i = 0 # counter
    for c in dna:
        print ('c:', c)
        if c == base:
            print ('True if test')
            i += 1
    return i

# Index Iteration
def count_v3(dna, base):
    i = 0 # counter
    for j in range(len(dna)):
        if dna[j] == base:
            i += 1
    return i

# While Loops
def count_v4(dna, base):
    i = 0 # counter
    j = 0 # string index
    while j < len(dna):
        if dna[j] == base:
            i += 1
        j += 1
    return i

# Summing a Boolean List
def count_v5(dna, base):
    m = []   # matches for base in dna: m[i]=True if dna[i]==base
    for c in dna:
        if c == base:
            m.append(True)
        else:
            m.append(False)
    return sum(m)

# Inline If Test
def count_v6(dna, base):
    m = []   # matches for base in dna: m[i]=True if dna[i]==base
    for c in dna:
        m.append(True if c == base else False)
    return sum(m)

# Using Boolean Values Directly
def count_v7(dna, base):
    m = []   # matches for base in dna: m[i]=True if dna[i]==base
    for c in dna:
        m.append(c == base)
    return sum(m)

# List Comprehensions
def count_v8(dna, base):
    m = [c == base for c in dna]
    return sum(m)

# Here it is tempting to get rid of the m variable and reduce the function body to a single line:
def count_v9(dna, base):
    return sum([c == base for c in dna])

# Using a Sum Iterator
#The DNA string is usually huge - 3 billion letters for the human species. 
#Making a boolean array with True and False values therefore increases the memory usage by a factor of two in our sample functions
#count_v5 to count_v9. Summing without actually storing an extra list is desirable. Fortunately, sum([x for x in s]) can be 
#replaced by sum(x for x in s), where the latter sums the elements in s as x visits the elements of s one by one. 
#Removing the brackets therefore avoids first making a list before applying sum to that list. 
#This is a minor modification of the count_v9 function:
def count_v10(dna, base):
    return sum(c == base for c in dna)

# Extracting Indices
# Instead of making a boolean list with elements expressing whether a letter matches the given base or not,
# we may collect all the indices of the matches. This can be done by adding an if test to the list comprehension:

def count_v11(dna, base):
    return len([i for i in range(len(dna)) if dna[i] == base])

# Using Python's Library
#Very often when you set out to do a task in Python, there is already functionality for the task in the object itself, 
# in the Python libraries, or in third-party libraries found on the Internet. Counting how many times a letter
#(or substring) base appears in a string dna is obviously a very common task so Python supports it by the syntax dna.count(base):

def count_v12(dna, base):
    return dna.count(base)

# For Print:
#We have here illustrated two alternative ways of writing out text where the value of variables are to be inserted in "slots" in the string:
# printf-style formatting
# print ('%s appears %d times in %s' % (base, n, dna))

# or (new) format string syntax
# print ('{base} appears {n} times in {dna}'.format(base=base, n=n, dna=dna))

# Efficiency Assessment
#Now we have 11 different versions of how to count the occurrences of a letter in a string.
#Which one of these implementations is the fastest? 
#To answer the question we need some test data, which should be a huge string dna.
#######################################################

def compare_efficiency(functions, dna, base):
    timing = []
    result = []
    for fun in functions:
        t0 = time.time()
        freq =fun(dna, base)
        t1 = time.time()
        result.append(( fun.__name__, freq, (t1-t0)))
    return result

import time
functions = [count_v1, count_v2, count_v3, count_v4, count_v5, count_v6, count_v7, count_v8, count_v9, count_v10, count_v11,
             count_v12]

def main():
    dna = generate_string(6000000)
    print(f"The random dna is: {dna}")
 
    base = "T"
    res= compare_efficiency(functions, dna, base )

    for item in res:
        print(f"function v{item[0]}= The frequency of {base} base is: {item[1]} with {item[2]} s cpu time!")
    

if __name__ == "__main__":
   main()