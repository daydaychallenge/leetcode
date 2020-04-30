

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        #### [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

        Given a string, find the length of the **longest substring** without repeating characters.

        **Example 1:**

        ```
        Input: "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.
        ```

        **Example 2:**

        ```
        Input: "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.
        ```

        **Example 3:**

        ```
        Input: "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
                     Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
        ```

        Parameters
        ----------
        s: str

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
        d = {}
        res = start = 0
        for i, c in enumerate(s):
            if c in d:
                start = max(start, d[c]+1)
            res = max(res, i-start+1)
            d[c] = i
        return res
