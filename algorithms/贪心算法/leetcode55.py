#lc55，跳跃游戏 https://leetcode.cn/problems/jump-game/


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0  # 当前能到达的最远位置
        for i in range(len(nums)):
            if i>maxReach:
                return False
            maxReach=max(maxReach,i+nums[i])
            if maxReach>=len(nums)-1:
                return True
        return False
