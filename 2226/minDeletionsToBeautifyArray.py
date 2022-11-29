from typing import List

class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        return minDelRecursive(nums, 0, 1)

def minDelRecursive(nums: List[int], count: int, index: int) -> int:
    if(index >= len(nums)-1):
        if(len(nums) % 2 != 0):
            return count+1
        return count
    elif(nums[index] == nums[index-1]):
        nums.pop(index)
        return minDelRecursive(nums, count+1, index)
    else:
        return minDelRecursive(nums, count, index+2)

sample = [1,1,2,3,5]
mySol = Solution()
print(mySol.minDeletion(sample))