class Solution:
        
    # Bottom Up Approach to DP:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # array to store best sub-scores
        table = [amount+1 for x in range(amount+1)]     # fill with amount+1 as an empty value
        table[0] = 0
        
        for i in range(0, amount+1):
            for coin in coins:  # check subtracting each coin from i
                if coin <= i:
                    remaining = i - coin
                    score = table[remaining] + 1    # use the already calculated remainder
                    table[i] = min(table[i], score) # set table[i] to least amount
        
        if table[amount] > amount:  # if we didn't find a solution, table[amount] will be amount + 1
            return -1
        
        return table[amount] # otherwise return our answer
        
     # Top down approach to DP: TLE
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         self.stored = {}
#         self.stored[0] = 0
#         sorted(coins, reverse=True)
#         r = self.recurse(coins, amount)
#         if r == sys.maxsize:
#             return -1
#         return r
    
#     def recurse(self, coins, leftover):
#         if leftover == 0:
#             return 0
#         if leftover in self.stored:
#             return self.stored[leftover] + 1
        
#         tempMin = sys.maxsize
#         for coin in coins:
#             if coin <= leftover:
#                 score = self.recurse(coins, leftover-coin)
#                 tempMin = min(tempMin, score)
            
#         if tempMin != sys.maxsize:
#             self.stored[leftover] = tempMin
#             return tempMin + 1
        
#         return tempMin
     
   
        
        
#   OLD ATTEMPT GREEDY SOLUTION:        
#         coins.sort()
        
#         length = len(coins)
#         topIndex = self.binarySearch(coins, length)
        
#         leftover = amount
#         return self.recurse(coins, topIndex, leftover)
        
            
#     #[1, 2, 5], 1, 6
#     def recurse(coins, index, leftover):
#         if coins[index] < leftover:
#             while leftover > coins[index]:
#                 leftover -= coins[index]
            
#             index -= 1
#         else:
#             while coins[index] > leftover:            
#                 index -= 1
#                 if index < 0:
#                     return -1
#             if coins[index] == leftover:
#                 return 1
        
#         outcome = self.recurse(coins, index, leftover)
#         if outcome == -1:
#             return -1
#         return outcome + 1
        
    
    
    
#     def binarySearch(coins, length):
#         low = 0
#         high = length-1
#         mid = high // 2
        
#         if coins[high] < amount:
#             return high
        
#         while coins[mid] != amount:
#             if coins[mid] < amount:
#                 low = mid
#             if coins[mid] > amount:
#                 high = mid
                
#             mid = (high + low) // 2
            
#             if low >= mid or high <= mid:
#                 break          
            
#         return mid
    
    # best =  
    # 6, 7, 8x, 9x, 10x, 21, 22, 23, 24, 25, 26
    # leftover = 14
    # leftover = 6
    # leftover = 0
    # 
    #
    # binary search for number <= leftover
    #
    #
    #
    #
