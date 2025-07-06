nums = [2,1,5,0,4,6]
n=len(nums)
i,j,k=0,0,0
def increasingTriplet(nums):
    for z in range(n):
        for i in range(0, n-2):
            for j in range(i + 1, n -1):
                for k in range(j+1, n):
                    if nums[i]<nums[j]<nums[k]:
                        return True

    return False

    
           
        
print(increasingTriplet(nums))