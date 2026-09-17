class Solution:
    hashmap={}
    def climbstairhelper(self,n):
        if n in self.hashmap:
            return self.hashmap[n]
        if n==0:
            return 1 
        if n<0:
            return 0
        res = self.climbstairhelper(n-1) + self.climbstairhelper(n-2)

        self.hashmap[n]=res
        return self.hashmap[n]

    def climbStairs(self, n: int) -> int:
        return self.climbstairhelper(n)
        