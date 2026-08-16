class Solution:
    def longestPalindrome(self, s: str) -> str:

        start,end=0,0
        for i in range(len(s)):
            len1=self.expand(s,i,i) # if odd substring
            len2=self.expand(s,i,i+1) # if even substring
            length=max(len1,len2)

            if length>(end-start):
                start=i-(length-1)//2
                end=i+length//2
        return s[start:end+1]

    # returns the len of the palindromic substring for the current index   
    def expand(self,s,l,r): 
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return r-l-1

    

        