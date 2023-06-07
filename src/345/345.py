class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel_idxs = []
        vowel_itms = []
        result = []
        all_vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

        for i in range(len(s)):
            result.append(s[i])
            if(s[i] in all_vowels):
                vowel_idxs.append(i)
                vowel_itms.append(s[i])

        vowel_itms.reverse()

        for i in range(len(vowel_idxs)):
            if(s[vowel_idxs[i]] in all_vowels):
                result[vowel_idxs[i]] = vowel_itms[i]

        return(''.join(result))