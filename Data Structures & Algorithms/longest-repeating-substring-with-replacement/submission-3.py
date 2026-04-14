from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxi = 0
        i = 0
        j = 0
        mp = defaultdict(int)
        maxf = 0
        maxi = 0
        while(i< len(s) and j < len(s)):
            mp[s[j]] += 1
            for key,val in mp.items():
                maxf = max(maxf, val )
            
            if ((j-i+1) - maxf <= k):
                maxi = max(maxi, (j-i+1))
            else:
                mp[s[i]] -= 1
                i += 1
            j += 1
                
        return maxi



        