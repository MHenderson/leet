class Solution(object):

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in nums2:
            for j in range(m):
                if nums1[j]>=i or nums1[j]==0:
                    nums1 = nums1[0:j] + [i] + nums1[j:m - 1]
                    break