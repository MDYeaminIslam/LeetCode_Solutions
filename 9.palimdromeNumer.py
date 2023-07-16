#Difiiculty: Easy
#Time Complexity: O(n) | Space Complexity: O(1)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
    
"""
#Difiiculty: Easy
#More efficient solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        
        reversed_num = 0
        original_num = x
        
        while x > 0:
            reversed_num = (reversed_num * 10) + (x % 10)
            x //= 10
        
        return original_num == reversed_num
"""