from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        """
        #### [539. Minimum Time Difference](https://leetcode.com/problems/minimum-time-difference/)

        Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum **minutes** difference between any two time points in the list.

        **Example 1:**

        ```
        Input: ["23:59","00:00"]
        Output: 1
        ```



        **Note:**

        1. The number of time points in the given list is at least 2 and won't exceed 20000.
        2. The input time is legal and ranges from 00:00 to 23:59.


        Parameters
        ----------
        timePoints: List[str]

        Returns
        -------
        int

        Examples
        --------
        >>> sol = Solution()
        >>> sol.findMinDifference(['23:59', '00:00'])
        1

        Notes
        -----

        References
        ---------

        """
        time_points = sorted([int(s[:2])*60 + int(s[-2:]) for s in timePoints])
        time_points.append(time_points[0]+1440)
        return min(a - b for a, b in zip(time_points[1:], time_points))
