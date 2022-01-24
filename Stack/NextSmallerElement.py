"""
Next Smaller Element
Difficulty Level : Medium
Last Updated : 06 Oct, 2021
Given an array, print the Next Smaller Element (NSE) for every element. The NSE for an element x is the first smaller element on the right side of x in array. Elements for which no smaller element exist (on right side), consider NSE as -1.
Examples:
a) For any array, rightmost element always has NSE as -1.
b) For an array which is sorted in increasing order, all elements have NSE as -1.
c) For the input array [4, 8, 5, 2, 25}, the NSE for each element are as follows.

Element         NSE
   4      -->    2
   8      -->    5
   5      -->    2
   2      -->   -1
   25     -->   -1
d) For the input array [13, 7, 6, 12}, the next smaller elements for each element are as follows.

  Element        NSE
   13      -->    7
   7       -->    6
   6       -->   -1
   12      -->   -1
"""

def nextSmallerElement(arr) :
    stack = []
    op = []
    for i in range(len(arr)-1, -1, -1) :
        if len(stack) == 0:
            op.append(-1)
        else :
            while len(stack) != 0 :
                if stack[-1] < arr[i] :
                    op.append(stack[-1])
                    break
                else:
                    stack.pop()
            if not stack :
                op.append(-1)


        stack.append(arr[i])
    return op[::-1]


print(nextSmallerElement([4, 8, 5, 2, 25]))
