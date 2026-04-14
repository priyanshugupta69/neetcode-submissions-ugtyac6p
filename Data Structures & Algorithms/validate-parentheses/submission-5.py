class Solution:
    def isValid(self, s: str) -> bool:
        mp = {}
        mp[']'] = '['
        mp[')'] = '('
        mp['}'] = '{'

        stack = []

        for param in s:
            if len(stack) > 0 and stack[-1] == mp.get(param, ''):
                stack.pop()
            else:
                stack.append(param)

        if len(stack) == 0:
            return True
        else:
            return False

        