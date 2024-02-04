# The Hamming distance between two equal-length strings of symbols is the number of positions 
# at which the corresponding symbols are different.

str1 = "abcdefg"
str2 = "cdf"
def find_pattern(str1, str2, trsh):
   
    count = 0
    for i in range(len(str1)- len(str2)+1):
        if hamming_dis(str1[i:i+len(str2)], str2)<= trsh:
             count+=1
    return count

def hamming_dis(text, pattern):
    count_mis = 0
    #print(text)
    for j in range(len(pattern)):
        if text[j] != pattern[j]:
            count_mis += 1
    #print(count_mis)
    return count_mis

trsh =1
print(find_pattern(str1,str2, trsh))
            

