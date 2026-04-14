from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) < 2:
            return 1
        
        mp = defaultdict(bool)
        beg = []

        for i in range(len(nums)):
            mp[nums[i]] = True

        for i in range(len(nums)):
            if mp[nums[i] - 1] != True:
                beg.append(nums[i])
        
        maxi = 1
        for i in range(len(beg)):
            count = 1
            num = beg[i]
            while(mp[num + 1] == True):
                count += 1
                num += 1
            maxi = max(count, maxi)

        return maxi

            
 
            


        