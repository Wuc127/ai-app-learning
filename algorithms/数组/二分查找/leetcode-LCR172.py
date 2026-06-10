from typing import List
class Solution:
    def countTarget(self, scores: List[int], target: int) -> int:
        left, right = 0, len(scores) - 1
        left_bound = -1
        while left<=right:
            mid = left + (right - left) // 2
            if scores[mid] == target:
                left_bound=mid
                right = mid - 1   # 继续向左找
            elif scores[mid] < target:
                left = mid+1
            elif scores[mid] > target:
                right = mid-1

        if left_bound == -1:
            return 0
        # 查找右边界
        left, right = 0, len(scores) - 1
        right_bound = -1
        while left <= right:
            mid = left + (right - left) // 2
            if scores[mid] == target:
                right_bound = mid
                left = mid + 1    # 继续向右找
            elif scores[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return right_bound - left_bound + 1

        # num=0
        # left, right = 0, len(scores) - 1
        # while left<=right:
        #     mid = left + (right - left) // 2
        #     if scores[mid] == target:
        #         a=mid
        #         b=mid-1
        #         while scores[a]==target:
        #             num+=1
        #             a+=1
        #         while scores[b]==target:
        #             num+=1
        #             b-=1
        #     elif scores[mid] < target:
        #         left=mid+1
        #     elif scores[mid] > target:
        #         right=mid-1
        # return num

            

