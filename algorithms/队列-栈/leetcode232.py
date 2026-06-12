# lc232 用栈实现队列
# https://leetcode.cn/problems/implement-queue-using-stacks/description/
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        # 先调用 peek 保证 s2 非空
        self.peek()
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            # 把 s1 元素压入 s2
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

