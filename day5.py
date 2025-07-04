# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


class Solution:   
    def reverseVowel(self, s:str)-> str:
        vowel=["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"] 
        string = list(s)
        left, right = 0 , len(string)-1
        while left < right:
            while left < right and string[left] not in vowel:
                left+=1
            while left < right and string[right] not in vowel:
                right-=1
            string[left], string[right] = string[right], string[left]
            left+=1
            right-=1

        return ''.join(string)
