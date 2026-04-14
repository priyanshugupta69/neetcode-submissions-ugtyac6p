from collections import defaultdict
import copy
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp = defaultdict(int)
        for i in s1:
            mp[i] += 1
        
        l = 0
        for r in range(len(s2)):
            if r - l + 1 > len(s1):
                if s2[l] in mp:
                    mp[s2[l]] += 1
                l += 1
            
            if s2[r] in mp:
                mp[s2[r]] -= 1

            if not any(val > 0 for val in mp.values()):
                return True
                
        return False
            


        