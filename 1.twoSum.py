class Solution(object):
    def twoSum(self, nums, target):
        if len(nums)<1:
            return False
        keys={}
        for i,v in enumerate(nums):
            if target-v in keys:
                return [keys[target-v],i]
            else:
                keys[v]=i
        return None