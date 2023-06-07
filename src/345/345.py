class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel_idxs = []
        vowel_itms = []
        result = []
        for i in range(len(s)):
            result.append(s[i])
            if(s[i] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]):
                vowel_idxs.append(i)
                vowel_itms.append(s[i])

        vowel_itms.reverse()

        for i in range(len(vowel_idxs)):
            print(i)
            if(s[vowel_idxs[i]] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]):
                result[vowel_idxs[i]] = vowel_itms[i]

        return(''.join(result))