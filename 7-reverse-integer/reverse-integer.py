class Solution:
    def reverse(self, x: int) -> int:
        st=str(x)
        if st[0].isalnum():
            left=0
        else:
            left=1
        li=list(st)
        right=len(st)-1
        while left<right:
            li[left],li[right]=li[right],li[left]
            left+=1
            right-=1
        new_str="".join(li)
        res= int(new_str)
        if -2**31<=res<= 2**31-1:
            return res
        return 0