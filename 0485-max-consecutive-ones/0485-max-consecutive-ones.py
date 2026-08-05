class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        l=0
        max_l=0
       
        for i in nums:
            if i==1:
                l+=1
                max_l=max(max_l,l)
            else:
                l=0    
        return max_l        
                
        