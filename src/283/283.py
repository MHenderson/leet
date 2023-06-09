class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums_z = [i for i, x in enumerate(nums) if x == 0]
        nums_nz = [i for i, x in enumerate(nums) if x != 0]
        nums_z.reverse()

        if(len(nums_nz) > 0 and len(nums_z) > 0):

            I = max(nums_z) # first zero from right (last zero from left)

            for I in nums_z:
                nums_nz = [i for i, x in enumerate(nums) if x != 0] 
                J = max(nums_nz) # last non-zero

                for k in range(I, J):
                    nums[k] = nums[k + 1]

                # there's only going to be one 0 that needs filling
                nums[J] = 0