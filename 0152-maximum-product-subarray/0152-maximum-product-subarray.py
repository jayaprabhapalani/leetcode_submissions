class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #using prefix and suffix prd we can calculate this in o(n)
        #reset them to 1 when their prd is 0
        prefix,suffix=1,1
        ans=float('-inf')
        n=len(nums)
        for i in range(n):
            if prefix==0:
                prefix=1
            if suffix==0:
                suffix=1

            prefix*=nums[i]
            suffix*=nums[n-1-i]
            ans=max(ans,max(prefix,suffix))
            
        return ans
