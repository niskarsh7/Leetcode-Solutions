class Solution:
    def maxProduct(self, n: int) -> int:
        li=[int(d) for d in str(n)]
        li.sort()
        return li[-1]*li[-2]
        