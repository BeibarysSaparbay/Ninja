class Solution:
    def subtractProductAndSum(self, n: int) -> int:        
        n = str(n)
        sum = 0
        res = 1
        for i in n:
            i = int(i)
            sum += i
            res *= i
        return res-sum