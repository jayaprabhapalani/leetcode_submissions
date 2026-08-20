class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ps=0
        mapp={0:1}
        cnt=0
        for i in range(len(nums)):
            ps+=nums[i]
            rem=ps%k

            if rem in mapp:
                cnt+=mapp.get(rem)
            
            mapp[rem]=mapp.get(rem,0)+1
            
        return cnt