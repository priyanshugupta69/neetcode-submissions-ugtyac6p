import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        i = 0
        j = 0
        mp = defaultdict(int)
        arr = []
        m = len(nums)
        while (i < m and j < m):
            if(nums[i] == nums[j]):
                mp[nums[i]] += 1
                j+=1
            else:
                i = j

        for key , val in mp.items():
            heapq.heappush(arr, (val, key))
            if len(arr) > k:
                heapq.heappop(arr)
        return [i[1] for i in arr]
 


        