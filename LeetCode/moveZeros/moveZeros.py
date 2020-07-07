from typing import List

def moveZeros1(nums):

    tam = len(nums)
    res = [0]*tam
    j = 0
    for num in nums:
        if num !=0:
            res[j]=num
            j+=1
    return res

def moveZeros2(nums):
    j = 0 
    for num in nums:
        if num != 0:
            nums[j]=num
            j+=1
    if j>0:
        for i in range(j,len(nums)):
            nums[i]=0
    return None

class Solution:
    def moveZeroes(self, nums):
        j = 0
        n = len(nums)
        for num in nums:
            if (num !=0):
                nums[j]=num
                j+=1
        for x in range(j,n):
            nums[x]=0
        return None




if __name__=="__main__":
    nums = [1,2,0,0,5,0,0,45,789]
    print(nums)
    a = Solution()
    a.moveZeroes(nums)
    print(nums)
    print(moveZeros1(nums))

