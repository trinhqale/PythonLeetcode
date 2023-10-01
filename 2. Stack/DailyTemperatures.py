'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100

'''
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []

        for idx, val in enumerate(temperatures):
            print("Iteration ", idx)
            print("Stack before loop: ", stack)
            print("res before loop: ", res)
            while stack and stack[-1][1] < val:
                index, value = stack.pop()
                res[index] = idx - index
                print("current res: ", res)
            stack.append([idx, val])
            print("Current Stack: ", stack)
            print('\n')
        return res 
        
# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    temperatures = [73,74,75,71,69,72,76,73]
    result1 = solution.dailyTemperatures(temperatures)
    print(result1)    


