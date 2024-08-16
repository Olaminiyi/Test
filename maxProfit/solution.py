# # say you have an array for which ith element is the price of a given stock on day i. 

# # if you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit

# # Note that you cannot sell a stock before you buy one

# # Example;

# # input: [7, 1, 5, 3, 6, 4]
# # output: 5

# # Explanation: Buy on day 2 (price =1) and sell on day 5 (pricee = 6), profit = 6-1 =5
# #              Not 7-1 = 6, as selling price needs to be larger than buying price.


# To solve this particular proble we are going to use (Two Pointers) initialize 2 pointers left and right(L, R)
# L = Buy
# R = sell

# L pointer on pointer on  value1   - 7
# R pointet on pointer  on  value2  - 1

# the values in the array represnt the price on each day to buy and sell 
# our pointer will be L and R, left pointer starting from the (leftmost) first (price or value) and L from the next Value 

# if difference in the price between (R - L) is negative that is loss i.e., R is less than L
# we move the pointer both(R & L)to the next value which is the 2 & 3 values, putting L on value 2 and R on value 3
# if difference in the price between (R - L) is +ve, that is a profit, the difference is our current maximum profit
# we will save it as maxProfit
# since our R is greater than L, we will not change the L pointer for now, the L will still remain on the second value while 
# our R pointer will move to to 4th value.

# if (R - L) is -Ve or < maxprofit:
#     maxProfit will not be updated
# else:
#     maxProfit = newValue 


# memory : o(1)
# Time : o(n)

# Days     1  2  3  4  5  6
# price   [7, 1, 5, 3, 6, 4]

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1

        return maxP
                
