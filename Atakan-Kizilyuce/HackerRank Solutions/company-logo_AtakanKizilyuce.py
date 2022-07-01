'''
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string

, which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

    Print the three most common characters along with their occurrence count.
    Sort in descending order of occurrence count.
    If the occurrence count is the same, sort the characters in alphabetical order.

'''
#librarys
import sys
from collections import Counter

#code
if __name__=='__main__':
    string = input().strip()
    sortit1 = Counter(string)
    sortit2 = sorted(sortit1.items(), key = lambda c: (-c[1], c[0]))[:3]

    print("\n".join(c[0]+" "+str(c[1]) for c in sortit2))

    
''' 
    sample input: aabbbccde

    sample output: b 3
                   a 2
                   c 2
'''
