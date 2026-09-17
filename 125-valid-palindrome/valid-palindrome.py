class Solution(object):
    def isPalindrome(self, s):
        clean_s = []
        for character in s:
            if character.isalnum():
                clean_s.append(character.lower())
        return clean_s == clean_s[::-1]