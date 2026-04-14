class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = 1000000000
        maxi = 0

        for price in prices:
            mini = min(mini, price)
            maxi = max(maxi, (price - mini))
        return maxi            


        