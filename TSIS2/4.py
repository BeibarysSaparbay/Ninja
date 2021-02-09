gain = [-5,1,5,0,-7]
ex = []
ex.append(0)
for i in range(0,len(gain)):
        tmp = ex[i] + gain[i]
        ex.append(tmp)
print(max(ex))


"""
class Solution(object):
    def largestAltitude(self, gain):
        ex = []
        ex.append(0)
        for i in range(0,len(gain)):
                tmp = ex[i] + gain[i]
                ex.append(tmp)
        return max(ex)

"""