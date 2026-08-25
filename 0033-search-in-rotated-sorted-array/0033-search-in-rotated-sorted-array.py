class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            m=l+(r-l)//2
            if nums[m]==target:
                return m
            #if left sorted 
            if nums[m]>=nums[l]:
                if target>=nums[l] and nums[m]>target:
                    r=m-1
                else:
                    l=m+1
            else: #right sorted arr
                if target<=nums[r] and nums[m]<target :
                    l=m+1
                else:
                    r=m-1
        return -1

                
        