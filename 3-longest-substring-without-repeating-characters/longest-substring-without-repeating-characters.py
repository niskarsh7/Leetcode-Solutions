class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        maxx=0
        se=set()
        while j < len(s):
            c=s[j]
            while c in se:
                se.remove(s[i]) 
                i+=1
            se.add(c)
            maxx=max(maxx,j-i+1)
            j+=1
        return maxx