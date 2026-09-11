class Solution:
    hashmap={}
    def fib(self, n: int) -> int:
        if n in self.hashmap:
            return self.hashmap[n]
        if n<=1:
            return n 
        res=self.fib(n-1)+self.fib(n-2)
        self.hashmap[n]=res
        return self.hashmap[n]