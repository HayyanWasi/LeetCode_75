string = "hello  world is mad at me i".split()

def reverse_string(string):
    left, right  = 0, len(string)-1
    while left<right:
            string[left], string[right] = string[right], string[left]
            left+=1
            right-=1

    return ' '.join(string)

# chatgpt code
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         return ' '.join(s.split()[::-1])