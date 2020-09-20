
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        """
        #### [564. Find the Closest Palindrome](https://leetcode.com/problems/find-the-closest-palindrome/)

        Given an integer n, find the closest integer (not including itself), which is a palindrome.

        The 'closest' is defined as absolute difference minimized between two integers.

        **Example 1:**

        ```
        Input: "123"
        Output: "121"
        ```



        **Note:**

        1. The input **n** is a positive integer represented by string, whose length will not exceed 18.
        2. If there is a tie, return the smaller one as answer.


        Parameters
        ----------
        n: str

        Returns
        -------
        str

        Examples
        --------

        Notes
        -----

        References
        ---------

        """
        length = len(n)
        candidates = {str(10**(length+1)+1), str(10**(length-1)-1)}
        prefix = int(n[:(length+1)//2])
        for m in map(str, (prefix-1, prefix, prefix+1)):
            candidates.add(m+m[::-1][(0, 1)[length & 1]:])
        candidates.discard(n)
        return min(candidates, key=lambda x: (abs(int(x)-int(n)), int(x)))


