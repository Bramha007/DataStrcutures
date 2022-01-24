"""
You have an empty sequence, and you will be given  queries. Each query is one of these three types:

1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.
Function Description

Complete the getMax function in the editor below.

getMax has the following parameters:
- string operations[n]: operations as strings

Returns
- int[]: the answers to each type 3 query

Input Format

The first line of input contains an integer, . The next  lines each contain an above mentioned query.

Constraints

Constraints



All queries are valid.

Sample Input

STDIN   Function
-----   --------
10      operations[] size n = 10
1 97    operations = ['1 97', '2', '1 20', ....]
2
1 20
2
1 26
1 20
2
3
1 91
3
Sample Output

26
91
"""


def getMax(operations):
    # Write your code here
    op = []
    stack = []
    max_ele = 0
    for ele in operations:
        args = list(map(int, ele.strip().split()))
        if args[0] == 1:
            max_ele = max(args[1], max_ele)
            stack.append(args[1])
        elif args[0] == 2:
            if stack.pop() == max_ele:
                if len(stack) > 0:
                    max_ele = max(stack)
                else:
                    max_ele = 0
        else:
            op.append(max_ele)
    return op
