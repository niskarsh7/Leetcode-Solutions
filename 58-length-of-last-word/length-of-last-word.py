class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        word=s.split()
        my_word=word[-1]
        return len(my_word)