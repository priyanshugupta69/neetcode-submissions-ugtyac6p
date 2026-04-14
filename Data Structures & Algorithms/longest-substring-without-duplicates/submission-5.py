from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if len(s) < 2:
            return 1
        maxi = 1
        i = 0
        j = 1

        vis = defaultdict(lambda: -1)

        vis[s[i]] = 0

        while(i < len(s) and j < len(s)):
            if vis[s[j]] != -1:
                i = max(i,vis[s[j]] + 1)
            maxi = max(maxi, (j - i + 1))
            vis[s[j]] = j
            j += 1

        return maxi


            


        