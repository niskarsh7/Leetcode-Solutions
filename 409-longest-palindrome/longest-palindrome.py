from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=Counter(s)
        ans=sum(v//2*2 for v in count.values())
        if ans<len(s):
            ans+=1
        return ans   
