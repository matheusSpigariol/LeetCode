def contains_duplicate(nums):
    solution = {}

    for index, num in enumerate(nums):
        if index == 0:
            solution[num] = index
            continue
        if solution.get(num) is not None:
            return True
        solution[num] = index
    return False
        

nums = [1, 2, 3, 1]
print(contains_duplicate(nums))

nums = [1, 2, 3, 4]
print(contains_duplicate(nums))
