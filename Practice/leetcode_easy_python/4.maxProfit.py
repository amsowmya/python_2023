from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prof=float('inf')
        max_prof=0

        for price in prices:
            min_prof=min(min_prof, price)
            max_prof=max(max_prof, price-min_prof)
        return max_prof
    
if __name__=="__main__":
    sol=Solution()
    items=[7,1,5,3,6,4]
    print(sol.maxProfit(items))