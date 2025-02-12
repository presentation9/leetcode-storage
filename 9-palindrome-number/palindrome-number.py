class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        r = 0
        test = x

        while test > 0:
            r = (r * 10) + (test % 10)
            test = test // 10

        return x == r
        