# LeetCode Binary Search Summary 二分搜索法小结
# https://www.cnblogs.com/grandyang/p/6854825.html

def lower_bound(arr, first, last, value):
# 适用于区间为空、答案不存在、有重复元素、搜索开/闭的上/下界等情况
    # search [first, last) 
    while first < last: # 搜索区间[first, last)不为空
        mid = first + (last - first) // 2
        if arr[mid] < value:
            first = mid + 1
        else: 
            last = mid
    # loop jump when first == last
    return first

def upper_bound(arr, first, last, value):
# 适用于区间为空、答案不存在、有重复元素、搜索开/闭的上/下界等情况
    # search [first, last) 
    while first < last: # 搜索区间[first, last)不为空
        mid = first + (last - first) // 2
        if value < arr[mid]:
            last = mid
        else: 
            first = mid + 1
    # loop jump when first == last
    return first

# upper bound could be better done by: 
# here the lower_bound and upper_bound differs only at if condition
def upper_bound(arr, first, last, value):
# 适用于区间为空、答案不存在、有重复元素、搜索开/闭的上/下界等情况
    # search [first, last) 
    while first < last: # 搜索区间[first, last)不为空
        mid = first + (last - first) // 2
        if arr[mid] <= value:
            first = mid + 1
        else: 
            last = mid
    # loop jump when first == last
    return first
