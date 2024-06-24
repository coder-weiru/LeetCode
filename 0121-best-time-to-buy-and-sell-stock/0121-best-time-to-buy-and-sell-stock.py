class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        map = {}
        map[0] = 0 
        for n in range(1, len(prices)):
            curr_p = prices[n] - prices[n-1]
            prev_p = map[n-1]
            if prev_p > 0:
                curr_p = curr_p + prev_p
            map[n] = curr_p
            if profit < curr_p:
                profit = curr_p
                
        return profit
            
            
            