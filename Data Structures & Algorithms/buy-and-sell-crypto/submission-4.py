class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for i in range(1,len(prices)):
            maxP = max(prices[i] - minBuy, maxP)
            minBuy = min(minBuy, prices[i])
        
        return maxP