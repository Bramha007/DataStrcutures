"""
You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. You can change the height of a stack by removing and discarding its topmost cylinder any number of times.

Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they are all the same height, then return the height.

Example

There are  and  cylinders in the three stacks, with their heights in the three arrays. Remove the top 2 cylinders from  (heights = [1, 2]) and from  (heights = [1, 1]) so that the three stacks all are 2 units tall. Return  as the answer.

Note: An empty stack is still a stack.

Function Description

Complete the equalStacks function in the editor below.

equalStacks has the following parameters:

int h1[n1]: the first array of heights
int h2[n2]: the second array of heights
int h3[n3]: the third array of heights
Returns

int: the height of the stacks when they are equalized
Input Format

The first line contains three space-separated integers, , , and , the numbers of cylinders in stacks , , and . The subsequent lines describe the respective heights of each cylinder in a stack from top to bottom:

The second line contains  space-separated integers, the cylinder heights in stack . The first element is the top cylinder of the stack.
The third line contains  space-separated integers, the cylinder heights in stack . The first element is the top cylinder of the stack.
The fourth line contains  space-separated integers, the cylinder heights in stack . The first element is the top cylinder of the stack.
Constraints

Sample Input

STDIN       Function
-----       --------
5 3 4       h1[] size n1 = 5, h2[] size n2 = 3, h3[] size n3 = 4
3 2 1 1 1   h1 = [3, 2, 1, 1, 1]
4 3 2       h2 = [4, 3, 2]
1 1 4 1     h3 = [1, 1, 4, 1]
Sample Output

5
"""


def equalStacks(h1, h2, h3):
    sum_h1 = sum(h1)
    sum_h2 = sum(h2)
    sum_h3 = sum(h3)
    print(h1, h2, h3)
    while True:
        if len(h1) == 0 or len(h2) == 0 or len(h3) == 0:
            return 0
        if sum_h1 == sum_h2 and sum_h2 == sum_h3:
            return sum_h1
        elif max(sum_h1, sum_h2, sum_h3) == sum_h1:
            sum_h1 = sum_h1 - h1[0]
            h1.pop(0)
        elif max(sum_h1, sum_h2, sum_h3) == sum_h2:
            sum_h2 = sum_h2 - h2[0]
            h2.pop(0)
        else:
            sum_h3 = sum_h3 - h3[0]
            h3.pop(0)


test1 = {
    'input': {
        'h1': [3, 2, 1, 1, 1],
        'h2': [4, 3, 2],
        'h3': [1, 1, 4, 1]
    },
    'output': 5
}

print(equalStacks(**test1["input"]))
