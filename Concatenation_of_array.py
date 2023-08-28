# Given an integer array nums of length n, you want to
# create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
#
# Specifically, ans is the concatenation of two nums arrays.
#
# Return the array ans.

nums = [1, 2, 1]


def getConcatenation(nums: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[i])
        for j in range(len(nums)):
            ans.append(nums[j])
        return ans


print(getConcatenation(nums))




