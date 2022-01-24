"""Find the nearest smaller numbers on left side in an array
Difficulty Level : Medium
Last Updated : 13 Apr, 2021
Given an array of integers, find the nearest smaller number for every element such that the smaller element is on left side.

Examples:

Input:  arr[] = {1, 6, 4, 10, 2, 5}
Output:         {_, 1, 1,  4, 1, 2}
First element ('1') has no element on left side. For 6,
there is only one smaller element on left side '1'.
For 10, there are three smaller elements on left side (1,
6 and 4), nearest among the three elements is 4.

Input: arr[] = {1, 3, 0, 2, 5}
Output:        {_, 1, _, 0, 2}
Expected time complexity is O(n). """


def nearestSmallestToLeft(arr):
    stack = []
    op = []
    for ele in arr:
        if len(stack) == 0:
            op.append(-1)
        else :
            while len(stack) != 0:
                if stack[-1] < ele:
                    op.append(stack[-1])
                    break
                else :
                    stack.pop()
            if not stack:
                op.append(-1)
        stack.append(ele)
    return op


test1 = {
    'input': {
        'arr': [1, 6, 4, 10, 2, 5]
    },
    'output': [-1, 1, 1, 4,  1, 2]
}
test2 = {
    'input': {
        'arr': [1, 3, 2, 4]
    },
    'output': [-1, 1, 1, 2]
}


print(nearestSmallestToLeft(**test2["input"]))


