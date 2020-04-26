#EX-2
#Write a Python program to remove duplicates from a list of lists.
import itertools
num = [[110, 120], [240], [330, 456, 425], [310, 220], [133], [240]]
print("Original List", num)
num.sort()
new_num = list(num for num,_ in itertools.groupby(num))
print("New List", new_num)
