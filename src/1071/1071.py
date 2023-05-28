# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
# Example 1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

class Solution(object):

    def divides(self, x, y):
        m = len(x)
        n = len(y)
        result = False
        if(n % m == 0):
            z = x * int(n / m)
            if(z == y):
                result = True
        return(result)

    # assume str1 is longer
    def gcd_(self, str1, str2):
        result = ""
        for i in range(1,len(str2) + 1):
            test_sub = str2[0:i]
            if(self.divides(test_sub, str1) and self.divides(test_sub, str2)):
                result = test_sub
        return(result)

    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        result=""
        if(len(str1) > len(str2)):
            result = self.gcd_(str1, str2)
        else:
            result = self.gcd_(str2, str1)
        return(result)
