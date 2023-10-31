from typing import List


def binarysearch(nums:List[int] , target: int) -> int:
    l,r = 0, len(nums)-1

    while l <= r:
        mid = (l+r) // 2
        if (nums[mid] == target):
            return mid
        if (nums[mid] < target):
            l = mid + 1
        else:
            r = mid - 1
    return -1





def search(nums: List[int], target: int) -> int:
    for i,n in enumerate(nums): 
        if n==target: return i
    return -1
def binsearch(nums: List[int], target: int)-> int:
    left, right = 0, len(nums) -1
    
    # array is sorted so mid is a pivot where we can incr/decr left right
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return -1
