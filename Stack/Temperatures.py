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
