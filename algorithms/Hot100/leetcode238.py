# https://leetcode.cn/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-100-liked

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        answer=[1]*n
        left=1
        for i in range(n):
            answer[i]=answer[i]*left
            left=nums[i]*left

        right=1
        for i in range(n-1,-1,-1):   #这里不能写for i in range(i+1,n)
            answer[i]=answer[i]*right
            right=nums[i]*right
        
        return answer

