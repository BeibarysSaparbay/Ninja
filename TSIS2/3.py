a = [1,1,1,1]
#[1,2,3,1,1,3]
cnt = 0 
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i] == a[j]:
            cnt += 1
print(cnt)

"""
class Solution(object):
    def numIdenticalPairs(self, nums):
        cnt = 0 
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    cnt += 1
        return cnt
"""