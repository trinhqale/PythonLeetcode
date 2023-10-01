'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        pass

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    input1 = ...  # Replace with the input for test case 1
    input2 = ...  # Replace with the input for test case 1
    expected_output1 = ...  # Replace with the expected output for test case 1
    result1 = solution.functionName(input1, input2)
    assert result1 == expected_output1, f"Test case 1 failed: {result1}"
    
    # Test case 2
    input1 = ...  # Replace with the input for test case 2
    input2 = ...  # Replace with the input for test case 2
    expected_output2 = ...  # Replace with the expected output for test case 2
    result2 = solution.functionName(input1, input2)
    assert result2 == expected_output2, f"Test case 2 failed: {result2}"
 