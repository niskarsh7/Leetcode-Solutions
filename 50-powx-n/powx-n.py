class Solution:
    def helper(self,x,n):
        if (n==1):
            return x
        if (n==0):
            return 1.0
        if (n <0):
            return 1/self.helper(x,-n)
        temp=self.helper(x,n//2)
        if (n%2==0):
            return temp*temp
        return x*temp*temp
    def myPow(self, x: float, n: int) -> float:
        return self.helper(x,n)