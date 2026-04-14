import math
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        have, need = 0 , len(set(t))
        dest, find = {}, {}
        mini = math.inf
        min_index = (-1,-1)
        for i in range(len(t)):
            dest[t[i]] = dest.get(t[i], 0) + 1
        
        i = 0
        for r in range(len(s)):
            if s[r] in dest:
                find[s[r]] = find.get(s[r], 0) + 1

                if dest[s[r]] == find[s[r]]:
                    have += 1

            print(find.get(s[r], -1), dest.get(s[r], -1))
            print(have, need)
            while(i <= r and have == need):
                if (r - i + 1) < mini:
                    mini = (r - i + 1)
                    min_index = (i, r)
                if s[i] in find:
                    find[s[i]] -= 1

                    if find[s[i]] < dest[s[i]]:
                        have -= 1
                i += 1

        print(min_index)
        if min_index == (-1,-1):
            return ""
        return s[min_index[0]:min_index[1] + 1]

                

                     

            

        

            

            
            

        