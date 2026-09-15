class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]



sol = Solution()

# Example 1
print(sol.twoSum([2, 7, 11, 15], 9))   # expected [0, 1]

# Example 2
print(sol.twoSum([3, 2, 4], 6))        # expected [1, 2]

# Example 3
print(sol.twoSum([3, 3], 6))           # expected [0, 1]

# Negative numbers
print(sol.twoSum([-1, -2, -3, -4, -5], -8))  # expected [2, 4]

# Zero target
print(sol.twoSum([0, 4, 3, 0], 0))     # expected [0, 3]