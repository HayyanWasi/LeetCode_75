# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t 
# (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2. 

import math

def gcd_of_strings(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""
    gcd_length = math.gcd(len(str1), len(str2))
    print(gcd_length,"GCD length")
    return str1[:gcd_length]  

print(gcd_of_strings("PQRPQR", "PQR"))

        