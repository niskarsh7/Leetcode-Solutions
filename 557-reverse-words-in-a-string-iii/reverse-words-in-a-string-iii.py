class Solution:
    def reverseWords(self, s: str) -> str:
        arr=s.split()
        i=0
        reverse_string=[w[::-1] for w in arr]
        new=" ".join(reverse_string)
        return new