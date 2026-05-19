class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_string = ''.join(char for char in s if char.isalnum()).lower()
        return alnum_string == alnum_string[::-1]