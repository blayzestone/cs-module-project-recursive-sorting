# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if start <= end:
        mid = (end + start) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

        return binary_search(arr, target, start, end)
    else:
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    return arr


# Your code here

