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

    # Here's how it works:
    #
    # You have your big box (the arr array) that you want to sort.
    # It's divided into three parts: the left part (from L to M),
    # the middle part (just after M), and the right part (from M+1 to R).
    def merge(arr, L, M, R):

        # this part creates two new arrays, left (from l to m) and right (from m to r)
        left, right = arr[L:M+1], arr[M+1:R+1]

        # now this part initializes 3 new variables, i, j and k.
        # i is used to actually track the position while iterating in the original 'arr' array
        # j is used to keep track of the current position in the 'left' array we just initiated. It starts at index 0
        # k is used to keep track of the current position in the right array. It also starts at the beginning, index 0
        i, j, k = L, 0, 0

        # This is a loop that continues as long as there are elements left in both the left and right arrays.
        while j < len(left) and k < len(right):

            # if the left[j] element is smaller than or equal to right[k], we take that element and add it to the big
            # array (arr[i])
            if left[j] <= right[k]:
                arr[i] = left[j]

                # after that, we move the pointer to the next element in the left array (next toy from the left box)
                j += 1

            # the right[k] element is bigger than the left[j] element, aka the toy from the right box is bigger than
            # the toy from the left box
            else:

                # takes the toy from the right box at position k and puts it into the main array 'big box' at position i
                # after comparing it to the left[j] element, we put the right[k] element into the big array since it is
                # the smaller one, as we just did the comparison in the 'if' up there
                arr[i] = right[k]

                # moving the pointer to the next element in the right array, picking the next toy from the right box
                k += 1

            # after adding an element from either the left array or the right array, we move the pointer to the next
            # spot so that we can pick another toy to add to the big array
            i += 1

        # if there still are toys in the left box (indexed by j), it means that they are larger than the ones in the
        # right box and need to be added to the big box
        while j < len(left):

            # adding one toy at a time
            nums[i] = left[j]

            # moving the pointers in case there aren't any elements in the left box (left array)
            j += 1
            i += 1

        # same thing, but for the right box/array
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

# Now, I will implement it in quicksort

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1



