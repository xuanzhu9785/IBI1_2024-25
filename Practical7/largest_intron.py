import re
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
x = re.findall(r'GT.+?AG',seq)
if x:
    largest_intron = max(x, key=len)
    print("the lenth of the largest intron in the sequence is ", len(largest_intron))
else:
    print("cannot find intron in this sequence")