def ProductExceptSelf(nums):
    '''
    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the division operation.

    

    Example 1:

    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]
    Example 2:

    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]
    

    Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    

    Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)'''
    
    result = [1 for _ in range(len(nums))]
    # make a prefix list [1,2,3,4] -> [1, 1 * 1, 1 * 1 * 2, 1 * 1 * 2 * 3] -> 
    prefix = 1
    for i in range(len(nums)):
        result[i] *= prefix
        prefix *= nums[i]

    #make a postfix list [1,2,3,4] -> [2 * 3 * 4 * 1, 3 * 4 * 1, 4 * 1, 1]
    postfix = 1  
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]
    return result

def main():
    nums1 = [1,2,3,4]
    nums1_expected = [24,12,8,6]
    nums2 = [-1, 1, 0, 3, -3]
    nums2_expected = [0, 0, 9, 0, 0]
    assert(ProductExceptSelf(nums1) == nums1_expected)
    assert(ProductExceptSelf(nums2) == nums2_expected)
    print("All test cases passed")

if __name__ == "__main__":
    main()