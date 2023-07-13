class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        word = list(s)
        length = len(s)
        left, right = 0, length - 1

        while left < right:
            if word[left] in vowels and word[right] in vowels:
                word[left], word[right] = word[right], word[left]
                left += 1
                right -= 1
            elif word[left] in vowels:
                right -= 1
            else:
                left += 1

        return ''.join(word)
