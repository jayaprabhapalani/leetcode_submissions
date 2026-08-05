class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        max_l=0
        i=0

        while(i<n):  
            if nums[i]==1:
                l+=1
                max_l=max(max_l,l)
            else:
                l=0
            i+=1    
        return max_l            
                
        