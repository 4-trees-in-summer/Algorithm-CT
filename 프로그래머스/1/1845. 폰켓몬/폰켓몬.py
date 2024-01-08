import collections

def solution(nums):
    answer = 0
    
    l = len(nums)//2
    return min(l, len(list(set(nums))))