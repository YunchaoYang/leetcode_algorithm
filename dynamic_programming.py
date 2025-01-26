# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 15:21:12 2023

@author: yangy
"""

# %%
# 0-1 knapsack
def knapsack_01(W, wt, val, N):
    dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]

    for i in range(N + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
        print(dp)
    return dp[N][W]

# Example usage:
val = [6, 8, 12, 8]
wt  = [1, 2, 3, 4]
W  = 6
n = len(val)
print(knapsack_01(W, wt, val, n))  # Output will be 220

#%%
# complete knapsack problem
def knapsack_complete_2D(W, wt, val, n):
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
        print(dp)
    return dp[n][W]

# Example usage:
val = [6, 8, 12, 8]
wt  = [1, 2, 3, 4]
W  = 6
n = len(val)
print(knapsack_complete_2D(W, wt, val, n))  # Output will be 300


# comments:
'''
If we compare the key difference is this line:
     dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w]) # 0-1
     dp[i][w] = max(val[i - 1] + dp[i    ][w - wt[i - 1]], dp[i - 1][w]) # complete


'''
    
# %%
# knapsack_complete with 1D array
# with rolling array
def knapsack_complete(W, wt, val, n):
    dp = [0 for _ in range(W + 1)]

    for i in range(n):
        for w in range(W + 1):
            if wt[i] <= w:
                dp[w] = max(dp[w], dp[w - wt[i]] + val[i])
        print(dp)      
    return dp[W]

# Example usage:
val = [6, 8, 12, 4]
wt  = [1, 2, 3, 4]
W  = 6
n = len(val)
print(knapsack_complete(W, wt, val, n))  # Output will be 300


# %%
# knapsack_01 with 1D array
# can also be done with 1D array,
# but in a reversed visiting sequence
# def knapsack_01_1D(W, wt, val, n):
#     dp = [0 for _ in range(W + 1)]

#     for i in range(n):
#         for w in range(W, wt[i]-1, -1):
#             dp[w] = max(dp[w], dp[w - wt[i]] + val[i])
#         print(dp)      
#     return dp[W]

def knapsack_01_1D(W, wt, val, n):
    dp = [0 for _ in range(W + 1)]

    for i in range(n):
        for w in range(W, wt[i] - 1, -1):
            dp[w] = max(dp[w], val[i] + dp[w - wt[i]])
    return dp[W]

# Example usage:
val = [6, 7, 9, 10]
wt = [2, 2, 3, 4]
W = 4
n = len(val)
print(knapsack_01_1D(W, wt, val, n))  # Output will be 13

#%%
# multiple 0-1 with 1D rolling array
def multiple_knapsack(W, wt, val, counts, n):
    dp = [0 for _ in range(W + 1)]

    for i in range(n):
        for k in range(counts[i]):  # Consider multiple instances of the item
            for w in range(W, wt[i] - 1, -1):
                dp[w] = max(dp[w], val[i] + dp[w -wt[i]])
    return dp[W]

# Example usage:
val = [6, 8, 12, 8]
wt = [1, 2, 3, 4]
cnt = [2, 2, 3, 4]
W = 7
n = len(val)
print(multiple_knapsack(W, wt, val, cnt, n))  # Output will be 26

# 时间复杂度：O(m × n × k)，m：物品种类个数，n背包容量，k单类物品数量
