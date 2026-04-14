import math
class MinStack:

    def __init__(self):
        self.stack = []
        self.mini_array = [math.inf]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mini_array.append(min(self.mini_array[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.mini_array.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mini_array[-1]

        
