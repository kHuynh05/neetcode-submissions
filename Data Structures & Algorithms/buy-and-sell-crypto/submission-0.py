class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            total = 0;
            for i in range(len(prices)-1):
                profit = max(prices[i+1:])
                print(profit)
                if(total < (profit - prices[i])):
                    total = profit - prices[i]
            return total;
        