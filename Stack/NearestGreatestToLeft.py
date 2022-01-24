"""
Given an array of integers, find the nearest (not considering distance, but value) greater element to the left of every element.

The elements for which no greater element exists on the left side, print -1.

Example:

Input:  {9, 4, 15, 6, 2, 10}
Output: {-1, 9, -1, 15, 6, 15}

Explanation:
The first element has nothing on the left side, so the answer for first is -1.
Second element 4 has 9 on the left which is greater than 4, so the answer is 9.
Third element 15 has nothing greater on the left side, so the answer is -1.
Fourth element 6 has 15 as the nearest greater element on the left, so the answer is 15
Similarly, we get values for the fifth and sixth elements.
"""


def nearestGreatestToLeft(arr):
    stack = list()
    op = []
    for i in range(len(arr)):
        if not stack:
            op.append(-1)
        else:
            while len(stack) != 0:
                if arr[i] < stack[-1]:
                    op.append(stack[-1])
                    break
                else:
                    stack.pop()
            if not stack:
                op.append(-1)
        stack.append(arr[i])
    return op


print(nearestGreatestToLeft([9, 4, 15, 6, 2, 10]))
