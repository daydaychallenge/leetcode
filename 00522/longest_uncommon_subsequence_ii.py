from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        """
        ### [522. Longest Uncommon Subsequence II](https://leetcode.com/problems/longest-uncommon-subsequence-ii/)

        Given a list of strings, you need to find the longest uncommon subsequence among them. The longest uncommon
        subsequence is defined as the longest subsequence of one of these strings and this subsequence should not
        be **any** subsequence of the other strings.

        A **subsequence** is a sequence that can be derived from one sequence by deleting some characters without
        changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty
        string is a subsequence of any string.

        The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence.
        If the longest uncommon subsequence doesn't exist, return -1.

        **Example 1:**

        ```
        Input: "aba", "cdc", "eae"
        Output: 3
        ```

        **Note:**

        1. All the given strings' lengths will not exceed 10.
        2. The length of the given list will be in the range of [2, 50].

        Notes
        -----

        References
        ---------

        """
        def is_sub_seq(t, s):
            s = iter(s)
            return all(c in s for c in t)
        for seq in sorted(strs, key=len, reverse=True):
            if sum(is_sub_seq(seq, t) for t in strs) == 1:
                return len(seq)

        return -1
