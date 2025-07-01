# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has,
#  and an integer extraCandies, denoting the number of extra candies that you have.
# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, 
# they will have the greatest number of candies among all the kids, or false otherwise.
# Note that multiple kids can have the greatest number of candies

from typing import List

candies:List[int] = [8, 4, 5, 7, 2]
extra_candies:int = 4
store_add_candies:List[int] = []
result:List[bool] = []
max_candies = max(candies)

if candies:
    for i in candies:
        add_candies = i + extra_candies
        store_add_candies.append(add_candies)

        if i + extra_candies >= max_candies:
            result.append(True)
        else:
            result.append(False)
    print(store_add_candies)
    print(result)

       


        









































        # print(f'kid one will have {i} + {extra_candies} = {adding}')





































