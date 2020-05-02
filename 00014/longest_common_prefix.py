from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        #### [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

        Write a function to find the longest common prefix string amongst an array of strings.
        
        If there is no common prefix, return an empty string `""`.
        
        **Example 1:**
        
        ```
        Input: ["flower","flow","flight"]
        Output: "fl"
        ```
        
        **Example 2:**
        
        ```
        Input: ["dog","racecar","car"]
        Output: ""
        Explanation: There is no common prefix among the input strings.
        ```
        
        **Note:**
        
        All given inputs are in lowercase letters `a-z`.


        Parameters
        ----------
        strs: List[str]

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
        shortest = min(strs, key=len)
        for i in range(len(shortest)):
            if any(s[i] != shortest[i] for s in strs):
                return shortest[:i]
        return shortest
