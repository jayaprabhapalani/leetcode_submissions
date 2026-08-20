class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #if the running sum <0 -reset it to zero
        max_sum=nums[0]
        cur_sum=0
        for num in nums:
            cur_sum+=num
            if cur_sum<0:
                
                max_sum=max(max_sum,cur_sum)
                cur_sum=0
            else:
                max_sum=max(max_sum,cur_sum)
                

        return max_sum        