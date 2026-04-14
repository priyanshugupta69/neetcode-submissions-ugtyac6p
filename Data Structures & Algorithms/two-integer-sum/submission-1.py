class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in mp:
                return [mp[ans], i]
            mp[nums[i]] = i
        return [-1,-1]   