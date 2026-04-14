class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        global_mul = 1
        zero_flag = False
        
        zero_count = 0
        for i in nums:
            if i ==0:
                zero_count += 1
            if zero_count > 1:
                return [0]*len(nums)

        for i in nums:
            if i != 0:
                global_mul *= i
            else:
                zero_flag = True
        
        ans = []
        for i in nums:
            if not zero_flag:
                ans.append(int(global_mul/i))
            else:
                ans.append(0 if i != 0 else int(global_mul))

        return ans


        