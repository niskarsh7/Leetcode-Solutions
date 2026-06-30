class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        string=s.split()
        i=0
        j=len(string)-1
        while i < j :
            string[i],string[j]=string[j],string[i]
            i+=1
            j-=1
        new=" ".join(string)
        return new