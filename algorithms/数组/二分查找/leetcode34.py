# # leetcode34，在排序数组中查找元素的第一个和最后一个位置，
# https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        left_bound = -1
        right_bound = -1
        while left<=right:
            mid = left + (right - left) // 2
            if nums[mid]==target:
                left_bound=mid
                right=mid-1
            if nums[mid]>target:
                right=mid-1
            if nums[mid]<target:
                left=mid+1
        if left_bound == -1:
            return[-1,-1]
        left, right = 0, len(nums) - 1
        right_bound = -1
        while left<=right:
            mid = left + (right - left) // 2
            if nums[mid]==target:
                right_bound=mid
                left=mid+1
            if nums[mid]>target:
                right=mid-1
            if nums[mid]<target:
                left=mid+1
        return [left_bound,right_bound]


