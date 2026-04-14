from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for i in strs:
            temp = [0]*26
            for j in i :
                pos = ord(j) - ord('a')
                temp[pos] += 1
            key = tuple(temp)
            mp[key].append(i)
        
        ans = []
        for i, val in mp.items():
            ans.append(val)

        return ans


            


        