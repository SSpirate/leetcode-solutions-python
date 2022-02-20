class Solution:
    def findNumbers(self, nums):
        count,counter,k = 0,0,0
        for i in range(0,len(nums)):
            k = nums[i]
            while(k>0):
                count=count+1
                n=n//10
            if (count % 2 ==0):
                counter + = 1
    return counter
        
