class Solution(object):
    def twoSum(self, nums, target):
        dict_={}
        i=0
        while i<len(nums):
            val= target - nums[i]
            if(val in dict_):
                return [dict_[val],i]
            dict_[nums[i]]=i
            i+=1
