class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt=0
        for i in range(len(s)):
            # Add palindromes centered at i (odd length)
            cnt+=self.expand(s,i,i)
            # Add palindromes centered between i and i+1 (even length)
            cnt+=self.expand(s,i,i+1)           
        return cnt

    # returns the cnt of the palindromic substring for the current index   
    def expand(self,s,l,r): 
        # Expand outwards as long as characters match
        cnt=0
        while l>=0 and r<len(s) and s[l]==s[r]:
            cnt+=1
            l-=1
            r+=1
        return cnt
        