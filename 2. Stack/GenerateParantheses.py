'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8'''








'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        
        def backtrack(open_count, closed_count):
            if n == open_count == closed_count:
                res.append(''.join(stack))
                return
            if open_count < n:
                stack.append('(')
                backtrack(open_count + 1, closed_count)
                stack.pop()
            if open_count > closed_count:
                stack.append(')')
                backtrack(open_count, closed_count + 1)
                stack.pop()
        backtrack(0,0)
        return res'''