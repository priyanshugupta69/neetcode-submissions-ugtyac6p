from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        m = len(nums)
        vis = defaultdict(bool)
        ans = []
        for i in range(m):
            mp = defaultdict(lambda: -1)
            for j in range(i+1, m):
                if mp[-(nums[j]+ nums[i])] != -1:
                    ans.append([nums[i],-(nums[j]+ nums[i]),nums[j]])
                mp[nums[j]] = j

        us = set()
        for i in ans:
            us.add(tuple(sorted(i)))

        return [list(t) for t in us ]



        