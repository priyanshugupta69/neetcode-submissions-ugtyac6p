class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mul = [1]*len(nums)
        suffix_mul = [1]*len(nums)
        prev = 1
        for i in range(1, len(nums)):
            prefix_mul[i] = prefix_mul[i-1] * nums[i-1]

        for i in range(len(nums) -2 , -1 , -1):
            suffix_mul[i] = suffix_mul[i+1] * nums[i+1]

        for i in range(len(nums)):
            nums[i] = prefix_mul[i] * suffix_mul[i]

        return nums



        