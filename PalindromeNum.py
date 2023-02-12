import math

num = 1237123
num2 = 1221
num3 = -12345
string = '1221'

class Solution(object):
    def isPalindrome(self, x):
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False


test = Solution()
test.isPalindrome(num)
test.isPalindrome(num2)
