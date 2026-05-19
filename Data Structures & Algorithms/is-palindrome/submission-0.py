class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = "".join(i.lower() for i in s if i.isalnum())
        reverse_str = clean_str[::-1]

        return clean_str == reverse_str