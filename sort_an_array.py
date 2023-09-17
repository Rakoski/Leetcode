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


# I will, then, use a merge-sort approach:

def sortArray(nums: list[int]) -> list[int]:
    def merge(arr, L, M, R):
        left, right = arr[L:M+1], arr[M+1:R+1]
        i, j, k = L, 0, 0

        while j < len(left) and k < len(right):
            if left[j] <= right[k]:
                arr[i] = left[j]
                j += 1
            else:
                arr[i] = right[k]
                k += 1
            i += 1
        while j < len(left):
            nums[i] = left[j]
            j += 1
            i += 1
        while k < len(right):
            nums[i] = right[k]
            k += 1
            i += 1

    def merge_sort(arr, LEFT, RIGHT):
        if LEFT == RIGHT:
            return arr

        MID = (LEFT + RIGHT) // 2
        merge_sort(arr, LEFT, MID)
        merge_sort(arr, MID + 1, RIGHT)
        merge(arr, LEFT, MID, RIGHT)

        return arr

    return merge_sort(nums, 0, len(nums) - 1)


