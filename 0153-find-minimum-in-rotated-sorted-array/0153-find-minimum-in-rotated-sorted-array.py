class Solution:
    def findMin(self, nums: List[int]) -> int:
        minn=nums[0]
        # for num in nums:
        #     minn=min(minn,num)
        
        # return minn
        for i in range(len(nums)):
            if nums[i]<=minn:
                minn=nums[i]
        return minn
