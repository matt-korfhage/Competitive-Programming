from typing import List

class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        index = 0
        count = 0
        for i in range(0, len(nums)):
            if(index >= len(nums)-1):
                break
            if(nums[index] == nums[index+1]):
                count = count + 1
                index = index - 1
            index = index + 2
        if((len(nums) - count) % 2 != 0):
            count = count + 1
        return count

sample = [1,1,2,2,3,3]
mySol = Solution()
print(mySol.minDeletion(sample))