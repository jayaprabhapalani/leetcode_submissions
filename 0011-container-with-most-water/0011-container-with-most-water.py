class Solution:
    def maxArea(self, height: list[int]) -> int:
        m_ar=0
        l=0
        r=len(height)-1
        while l<=r:
            w=r-l
            h=min(height[l],height[r])
            area=w*h
            m_ar=max(m_ar,area)
            
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return m_ar



            
            
        