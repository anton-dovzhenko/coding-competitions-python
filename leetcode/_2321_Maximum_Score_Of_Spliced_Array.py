import unittest
import numpy as np

from typing import List


class Solution:

    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        nums1 = np.array([0] + nums1)
        nums2 = np.array([0] + nums2)
        sums1 = nums1.cumsum()
        sums2 = nums2.cumsum()
        deltas12 = sums1 - sums2
        deltas21 = - deltas12
        deltas12 = np.flip(np.maximum.accumulate(np.flip(deltas12)))
        deltas21 = np.flip(np.maximum.accumulate(np.flip(deltas21)))
        best_n1 = sums1[-1]
        best_n2 = sums2[-1]
        for i in range(1, N):
            if nums1[i] > nums2[i]:
                best_n2 = max(best_n2, sums2[-1] + max(0, deltas12[i] - sums1[i - 1] + sums2[i - 1]))
            elif nums1[i] < nums2[i]:
                best_n1 = max(best_n1, sums1[-1] + max(0, deltas21[i] - sums2[i - 1] + sums1[i - 1]))
        return max(best_n1, best_n2)


class SolutionTest(unittest.TestCase):

    def test_maximumsSplicedArray(self):
        self.assertEqual(Solution().maximumsSplicedArray([60, 60, 60], [10, 90, 10]), 210)
        self.assertEqual(Solution().maximumsSplicedArray([20, 40, 20, 70, 30], [50, 20, 50, 40, 20]), 220)
