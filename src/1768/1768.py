# 1768. Merge Strings Alternately
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result=""

        n=len(word1)
        m=len(word2)

        for i in range(min(n,m)):
            result+=word1[i]+word2[i]

        if(n<m):
            result = result + word2[n:m]
        elif(n>m):
            result = result + word1[m:n]
        
        return(result)