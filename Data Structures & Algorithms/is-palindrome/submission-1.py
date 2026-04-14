import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = s.replace(" ", "").lower()
        st = re.sub(r'[^a-zA-Z0-9]', '', st)
        print(st)
        
        i = 0
        j = len(st) - 1

        while(i <= j):
            print(st[i], st[j], i, j)
            if st[i] != st[j]:
                return False
            i += 1
            j -= 1
        
        return True
        