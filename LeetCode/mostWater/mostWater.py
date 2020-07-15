from typing import List

class Solution:
    def mostWater(self, nums: List[int])->int:
        i = 0
        j = len(nums)-1
        max_area = 0
        while(i<j):
            max_area = max(max_area, min(nums[i],nums[j])*(j-i))
            if (nums[i]<nums[j]):
                i+=1
            else:
                j-=1
        
        return max_area


def mostWater(nums):
    i = 0
    j = len(nums)-1
    max_area = 0

    while(i<j):
        max_area = max(max_area, min(nums[i],nums[j])*(j-i))
        if (nums[i]<nums[j]):
            i+=1
        else:
            j-=1

    return max_area


if __name__=="__main__":
    print(mostWater([2,3,7,1,4,5,5,7,1,1,4]))
    print(mostWater([1,8,6,2,5,4,8,3,7]))
    print(Solution().mostWater([1,8,6,2,5,4,8,3,7]))