class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # store remainders instead of sum as we need the multiples here
        #store the ps in a var
        #initialize map with 0:-1 so that if we encounter the good subarr at the very first 2 index then we might need that to calculate the len of the subarr
        mapp={0:-1}
        ps=0
        for i in range(len(nums)):
            ps+=nums[i]
            rem=ps%k
            if rem in mapp:
                if i-mapp[rem]>=2:
                    return True
            else:
                mapp[rem]=i
        return False
           

        