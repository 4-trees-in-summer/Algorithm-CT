def solution(nums):
    answer = 0
    l = len(nums)//2
    nums = set(nums)
    
    if l >= len(nums) :
        return len(nums)
    else :
        return l