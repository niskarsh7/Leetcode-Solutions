class Solution:
    def helper(self,n,k,flip):
        if (n==1):
            return 0 if flip%2==0 else 1
        if (k%2==0):
            return self.helper(n-1,k//2,flip+1)
        return self.helper(n-1,(k+1)//2,flip)
    def kthGrammar(self, n: int, k: int) -> int:
        return self.helper(n,k,0)
        