# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         n = len(nums)
#         left_product = [1] * n
#         right_product = [1] * n
#         output = [1] * n
        
#         for i in range(1, n):
#             left_product[i] = left_product[i - 1] * nums[i - 1]
        
#         for i in range(n - 2, -1, -1):
#             right_product[i] = right_product[i + 1] * nums[i + 1]
        
#         for i in range(n):
#             output[i] = left_product[i] * right_product[i]
        
#         return output


def main(nums):
    n = len(nums)
    ans = []

    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= nums[j]
        ans.append(product)

    return ans

nums = [1, 2, 3, 4]
print(main(nums))  

