
class Solution:
    def reorganizeString(self, S: str) -> str:
        """
        #### [767. Reorganize String](https://leetcode.com/problems/reorganize-string/)

        Given a string `S`, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

        If possible, output any possible result. If not possible, return the empty string.

        **Example 1:**

        ```
        Input: S = "aab"
        Output: "aba"
        ```

        **Example 2:**

        ```
        Input: S = "aaab"
        Output: ""
        ```

        **Note:**

        - `S` will consist of lowercase letters and have length in range `[1, 500]`.


        Parameters
        ----------
        S: str

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
        from collections import Counter
        lens, counts = len(S), Counter(S)
        half = (lens + 1) // 2
        pairs = counts.most_common()
        _, max_cnt = pairs[0]
        if max_cnt - 1 > lens - max_cnt:
            return ''
        A = list(''.join(k*v for k, v in pairs))
        ans = ['']*lens
        ans[::2], ans[1::2] = A[:half], A[half:]
        return ''.join(ans)
