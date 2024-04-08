def two_sum(nums, target):
    solution = {}

    for index, num in enumerate(nums):
        if solution.get(num) is not None:
            return [solution.get(num), index]
        solution[target-num] = index

nums = [7, 1, 5, 8]
target = 12

print(two_sum(nums, target))
