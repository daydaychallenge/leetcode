from typing import List


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        """
        #### [992. Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/)

        Given an array `A` of positive integers, call a (contiguous, not necessarily distinct) subarray of `A` *good* if the number of different integers in that subarray is exactly `K`.

        (For example, `[1,2,3,1,2]` has `3` different integers: `1`, `2`, and `3`.)

        Return the number of good subarrays of `A`.



        **Example 1:**

        ```
        Input: A = [1,2,1,2,3], K = 2
        Output: 7
        Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
        ```

        **Example 2:**

        ```
        Input: A = [1,2,1,3,4], K = 3
        Output: 3
        Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
        ```

        **Note:**

        1. `1 <= A.length <= 20000`
        2. `1 <= A[i] <= A.length`
        3. `1 <= K <= A.length`



        Parameters
        ----------
        A: List[int]
        K: int

        Returns
        -------
        int

        Examples
        --------

        Notes
        -----

        References
        ---------

        """
        from collections import Counter

        class Window:
            def __init__(self):
                self.counts = Counter()
                self.non_zero = 0

            def add(self, x):
                self.counts[x] += 1
                if self.counts[x] == 1:
                    self.non_zero += 1

            def remove(self, x):
                self.counts[x] -= 1
                if self.counts[x] == 0:
                    self.non_zero -= 1

        left1 = left2 = res = 0
        window1 = Window()
        window2 = Window()

        for n in A:
            window1.add(n)
            window2.add(n)

            while window1.non_zero > K:
                window1.remove(A[left1])
                left1 += 1

            while window2.non_zero >= K:
                window2.remove(A[left2])
                left2 += 1

            res += left2 - left1

        return res


