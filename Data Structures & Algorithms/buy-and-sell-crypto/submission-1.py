class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = -1
        for n in prices:
            if n < lowest:
                lowest = n
            if profit < n - lowest:
                profit = n - lowest

        return profit

            
        