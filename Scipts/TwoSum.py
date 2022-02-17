def TwoSum(nums:list[int], target:int) -> list[int]:
    values = {}
    for i, n in enumerate(nums):
        if target-n in values.keys():
            return [values[target-n], i]
        if n not in values.keys():
            values[n] = i
    # For default case where there is no solution, return -1 and -1
    return [None, None]

# Test if this works
nums = [2,7,11,15]
target = 9
indices = TwoSum(nums, target)
print(f"Two numbers that add to {target} are {nums[indices[0]]} and {nums[indices[1]]}.")

