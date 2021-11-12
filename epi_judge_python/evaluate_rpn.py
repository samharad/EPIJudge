import collections

from test_framework import generic_test

operators = {"+": lambda a, b: a + b,
             "-": lambda a, b: a - b,
             "*": lambda a, b: a * b,
             "/": lambda a, b: a // b}


def evaluate(expression: str) -> int:
    words = expression.split(",")

    stack = collections.deque()
    for word in words:
        operator = operators.get(word, None)
        if operator:
            b = int(stack.pop())
            a = int(stack.pop())
            res = operator(a, b)
            stack.append(res)
        else:
            stack.append(word)
    return int(stack[0])


if __name__ == '__main__':
    generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                   evaluate)
