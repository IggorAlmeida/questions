from typing import List

class Solution:
    def validMountainArray(self, A: List[int])->bool:
        if(len(A) < 3):
            return False
        i=1
        while(i<len(A) and A[i]>A[i-1]):
            i+=1
        if(i==1 or i==len(A)):
            return False
        while(i<len(A) and A[i]<A[i-1]):
            i+=1
        return (i==len(A))



def valid_mountain(nums):

    i=1
    while(i<len(nums) and nums[i]>nums[i-1]):
        i+=1
    if(i==1 or i==len(nums)):
        return False
    while(i<len(nums) and nums[i]<nums[i-1]):
        i+=1
    return i==len(nums)


if __name__ =="__main__":

    array_teste = [1,2,1]
    print(valid_mountain(array_teste))

    # sol = Solution()
    print(Solution().validMountainArray(array_teste))
