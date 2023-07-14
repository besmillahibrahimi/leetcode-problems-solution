class Solution:
    def reverseWords(self, s: str) -> str:
        tokens = reversed(s.split())
        return ' '.join(tokens)
