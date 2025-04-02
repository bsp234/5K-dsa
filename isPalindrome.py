class Solution:
    def isPalindrome(self, x: int) -> bool:
      changeToString = str(x)
      return changeToString[::-1] == str(x)
        
