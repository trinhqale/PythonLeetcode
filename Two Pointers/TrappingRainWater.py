'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105'''
'''
Hints: 
1. find min of (max of both left and right)
2. 
'''
def TrappingRainWater(height):
    water = 0
    l, r = 0, len(height) - 1
    maxLeft = height[l]
    maxRight = height[r]

    while l < r:
        if maxLeft <= maxRight:
            l += 1
            maxLeft = max(maxLeft, height[l])
            water += (maxLeft - height[l])
        else:
            r -= 1
            maxRight = max(maxRight, height[r])
            water += (maxRight - height[r])
    return water

def main():
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(TrappingRainWater(height))

if __name__ == "__main__":
    main()