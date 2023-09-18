'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109'''

def LongestSequence(nums):
    longest = 0
    numSet = set(nums)
    for i in numSet:
        if i - 1 not in numSet: # first in sequence
            currentLength = 0
            while (i + currentLength) in nums:
                currentLength += 1
            longest = max(longest, currentLength)
    return longest
            

def main():
    tests = []
    tests.append([100,4,200,1,3,2])
    tests.append([0,3,7,2,5,8,4,6,0,1])
    tests.append([0,2,4,6,8,10])
    tests.append([])
    answers = []
    answers.append(4)
    answers.append(9)
    answers.append(1)
    answers.append(0)
    for i in range(len(tests)):
        if LongestSequence(tests[i]) == answers[i]:
            print("Test ", i, " passed")
        else:
            print("Test ", i, " failed")

if __name__ == "__main__":
    main()