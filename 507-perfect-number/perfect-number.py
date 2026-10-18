class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<=1:
            return False
        summ=1
        for i in range(2, isqrt(num)+1):
            if num%i==0:
                summ+=i
                if i!=num//i:
                    summ+=num//i
        return summ==num