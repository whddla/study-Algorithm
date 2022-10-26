def solution(nums):
    li = []
    for i in nums:
        if len(nums) / 2 == len(li):
            break 
        if not i in li:
            li.append(i)
        
    return len(li)

print(solution([3,1,2,3]))