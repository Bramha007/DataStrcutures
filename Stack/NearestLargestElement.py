from StackImplementation import Stack

"""Given an array, print the Next Greater Element (NGE) for every element. The Next greater Element for an element x is
the first greater element on the right side of x in the array. Elements for which no greater element exist, consider the
next greater element as -1.

Examples:

For an array, the rightmost element always has the next greater element as -1.
For an array that is sorted in decreasing order, all elements have the next greater element as -1.
For the input array [4, 5, 2, 25], the next greater elements for each element are as follows."""


def find_nearest_largest_ele(arr):
    op = list()
    stack = Stack()
    for i in range(len(arr) - 1, -1, -1):
        if stack.isEmpty():
            op.append(-1)
        elif not stack.isEmpty() and stack.peek() > arr[i]:
            op.append(stack.peek())
        elif not stack.isEmpty() and stack.peek() <= arr[i]:
            while not stack.isEmpty():
                if stack.peek() > arr[i]:
                    op.append(stack.peek())
                    break
                else:
                    stack.pop()
            if stack.isEmpty(): op.append(-1)
        stack.push(arr[i])
    stack.emptyStack()
    return op[::-1]


tests = []
test1 = {
    'input': {
        'arr': [13, 1, 10, 7, 14, 3, 10, 0]
    },
    'output': [14, 10, 14, 14, -1, 10, -1, -1]
}
test2 = {
    'input': {
        'arr': [1, 3, 2, 4]
    },
    'output': [3, 4, 4, -1]
}
tests.append(test1)
tests.append(test2)

for test in tests:
    print(find_nearest_largest_ele(**test["input"]) == test["output"])
