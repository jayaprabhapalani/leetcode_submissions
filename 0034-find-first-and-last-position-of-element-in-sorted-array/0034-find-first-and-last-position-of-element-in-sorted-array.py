class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        idx1=self.find_first(nums,target)
        idx2=self.find_last(nums,target)

        return [idx1,idx2]

    def find_first(self,nums,target):
        l=0
        r=len(nums)-1
        ans=-1 # init with -1 so if no idx we can return -1
        while(l<=r):
            m=l+(r-l)//2
            if nums[m]==target:
                ans=m
                r=m-1
            elif nums[m]<target:
                l=m+1
            else:
                r=m-1
        return ans

    def find_last(self,nums,target):
        l=0
        r=len(nums)-1
        ans=-1 # init with -1 so if no idx we can return -1
        while(l<=r):
            m=l+(r-l)//2
            if nums[m]==target:
                ans=m
                l=m+1
            elif nums[m]>target:
                r=m-1
            else:
                l=m+1
        return ans



        
        