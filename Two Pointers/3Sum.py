def ThreeSum(nums):
    nums.sort()
    result = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return result

def main():
    tests = []
    tests.append([-1,0,1,2,-1,-4])
    tests.append([0,1,1])
    tests.append([0,0,0])
    answers = []
    answers.append([[-1,-1,2],[-1,0,1]])
    answers.append([])
    answers.append([[0,0,0]])

    for i in range(len(tests)):
        if ThreeSum(tests[i]) == answers[i]:
            print("Test ", i, " passed")
        else:
            print("Test ", i, " failed")

if __name__ == "__main__":
    main()