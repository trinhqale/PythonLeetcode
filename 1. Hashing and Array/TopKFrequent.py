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
