import copy
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for i in range(len(strs)):
            temp = sorted(strs[i])
            temp = "".join(temp)
            if temp in mp:
                mp[temp].append(strs[i])
            else:
                mp[temp] =  [strs[i]]
        
        ans = []
        for key, val in mp.items():
            ans.append(val)
        return ans

            


        