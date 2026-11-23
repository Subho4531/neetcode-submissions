class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join(c.lower() for c in s if c.isalnum() and c!=" ")

        for i, w in enumerate(s):
            if s[i] != s[len(s) - i - 1]:
                return False

        return True
