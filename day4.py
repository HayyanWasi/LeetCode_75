# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, 
# return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
# from typing import List

from typing import List

def can_place_flower(flower_bed: List[int], n: int) -> bool:
    if n == 0:
        return True

    for i in range(len(flower_bed)):
        if flower_bed[i] == 0:
            check_left = (i == 0) or (flower_bed[i - 1] == 0)
            check_right = (i == len(flower_bed) - 1) or (flower_bed[i + 1] == 0)

            if check_left and check_right:
                flower_bed[i] = 1  
                n -= 1
                if n == 0:
                    return True
                
    return n == 0
