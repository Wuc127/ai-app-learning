# leetcode76 题最小覆盖子串，https://leetcode.cn/problems/minimum-window-substring/
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, window = {}, {}
        for c in t:
            if c in need:
                need[c] = need[c] + 1   # 键存在，值+1
            else:
                need[c] = 0 + 1         # 键不存在，先初始化为0，再+1
        
        left = 0
        right = 0
        valid = 0   # 判断左侧窗口是否要收缩
        start = 0   # 记录最小覆盖子串的起始索引
        length = float('inf')   # 记录最小覆盖子串长度
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                if c in window:
                    window[c]= window[c]+1
                else:
                    window[c]= 0 + 1
                if window[c] == need[c]:
                    valid += 1

            # 判断左侧窗口是否要收缩
            while valid == len(need):
                if right - left < length:# 在这里更新最小覆盖子串
                    start = left
                    length = right - left
                d = s[left]# d 是将移出窗口的字符
                left += 1# 缩小窗口
                # 进行窗口内数据的一系列更新
                if d in need: #1. 只有当移出的字符是需要的字符时，才处理
                    if window[d] == need[d]:    # 2. 如果移出前，这个字符的数量刚好满足要求
                        valid -= 1      # 3. 那么移出后就不再满足，valid 减 1
                    window[d] -= 1      # 4. 窗口内该字符数量减 1

        # 返回最小覆盖子串
        return "" if length == float('inf') else s[start: start + length]







