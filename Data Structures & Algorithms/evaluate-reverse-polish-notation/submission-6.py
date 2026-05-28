import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+" : operator.add, "-" : operator.sub, "*" : operator.mul, "/" : operator.truediv}

        for s in tokens:
            if s in ops:
                second = stack.pop()
                first = stack.pop()
                stack.append(int(ops[s](first, second)))
            else:
                stack.append(int(s))

        return stack.pop()
