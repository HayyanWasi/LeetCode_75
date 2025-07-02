# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t 
# (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2. 

import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:                            #to check the patten
            return ""                                             #if not pattern return ""
        return str1[: math.gcd(len(str1), len(str2))]             #taking length GCD of both strings and extract the strings of that length

sol = Solution()
print(sol.gcdOfStrings("ABCABC", "ABC"))  

        