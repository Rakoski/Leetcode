# Given an array of integer nums, sort the array in ascending order and return it without using any built-in functions
# and having a n(log n) complexity

# This means that insertion sort will not work, which was what I was studying since this: will be o(n^2)

class Solution:
    def sort_array(self, nums: list[int]) -> list[int]:
        for c in range(1, len(nums)):
            current_number = nums[c]
            for i in range(c -1, -1, -1):
                if nums[i] > current_number:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                else:
                    nums[i + 1] = current_number
                    break

        return nums




