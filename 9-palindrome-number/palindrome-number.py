class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0 :
            li=[int(d) for d in str(x)]
            return li==li[::-1]
        return False