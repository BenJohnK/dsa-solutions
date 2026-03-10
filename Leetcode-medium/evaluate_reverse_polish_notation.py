'''
150. Evaluate Reverse Polish Notation
Solved
Medium
Topics
premium lock icon
Companies
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
'''
import math

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators_set = {'+', '-', '*', '/'}
        for token in tokens:
            if token not in operators_set:
                stack.append(int(token))
            else:
                p = stack.pop()
                q = stack.pop()
                if token == "+":
                    stack.append(q+p)
                elif token == '-':
                    stack.append(q-p)
                elif token == '*':
                    stack.append(q*p)
                else:
                    value = q/p
                    if value < 0:
                        stack.append(math.ceil(value))
                    elif value >= 0:
                        stack.append(math.floor(value))
        return stack[0]
    
obj = Solution()
print(obj.evalRPN(["4","13","5","/","+"]))