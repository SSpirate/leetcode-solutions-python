class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        fin = 0
        count = 0
        for n in nums:
            if n == 1:
                count = count + 1
                if count > fin:
                    ans = count
            else:
                count = 0
        return fin
