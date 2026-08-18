class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res=[1]
        rprd=1
        for i in range(1,len(nums)):
            res.append(nums[i-1]*res[i-1])
        
        for i in range(len(nums)-1,-1,-1):
            res[i]*=rprd
            rprd*=nums[i]
        return res

        
        