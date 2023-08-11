from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        '''
        Do not return anything, modify nums in-place
        '''
        prev_idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                hold = nums[prev_idx]
                nums[prev_idx] = nums[i]
                nums[i] = hold
                prev_idx+=1
            print(nums)


if __name__ == "__main__":
    sol = Solution()
    list1 = [0,1,0,3,12]
    sol.moveZeroes(list1)