from typing import List

# one pass solution 
# simply define minumum as i@0 then as we pass through i see if curr max is > than curr price - min 
# or define min as curr price if its lower
def maxProfit(prices: List[int]) -> int:
    if not prices:
        return 0
    maxp = 0
    minp = prices[0]
    for p in prices:
        if p < minp:
            minp = p
        else:
            maxp = max(maxp, p - minp)
    return maxp

def maxProfitSW(prices: List[int]) -> int:
    if not prices: return 0
    i,j = 0, 1
    maxp = 0
    while j < len(prices):
        if prices[i] < prices[j]:
            maxp = max(maxp, prices[i] - prices[j])
        else:
            i = j
        j += 1
    return maxp 
