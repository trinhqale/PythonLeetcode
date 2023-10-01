def TopKFrequent(nums, k):
    numMap = {}

    for num in nums:
        if num not in numMap:
            numMap[num] = 0
        numMap[num] += 1

    countList = [[] for _ in range(len(nums) + 1)]
    for i in numMap:
        countList[numMap[i]].append(i)

    result = []
    for i in range(len(countList) - 1, 0, -1):
        if len(countList[i]) > 0:
            result += countList[i]
        if len(result) == k:
            return result
    return None


def main():
    nums = [1,1,1,2,2,3]
    k = 2
    print(TopKFrequent(nums, k))
    print(TopKFrequent([1], 1))

if __name__ == "__main__":
    main()


'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''