#this program accepts a list and a target as parameter
#it then parses the list and adds two items in the list together
# until it reaches the target
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                

solutionInstance = Solution()

result = solutionInstance.twoSum([2,7,11,15], 9)

