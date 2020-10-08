

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        """
        ### [1081. Smallest Subsequence of Distinct Characters](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/)

        Return the lexicographically smallest subsequence of `s` that contains all the distinct characters of `s` exactly once.

        **Note:** This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/


        **Example 1:**

        ```
        Input: s = "cdadabcc"
        Output: "adbc"
        ```

        **Example 2:**

        ```
        Input: s = "abcd"
        Output: "abcd"
        ```

        **Example 3:**

        ```
        Input: s = "ecbacba"
        Output: "eacb"
        ```

        **Example 4:**

        ```
        Input: s = "leetcode"
        Output: "letcod"
        ```



        **Constraints:**

        - `1 <= s.length <= 1000`
        - `s` consists of lowercase English letters.


        Notes
        -----

        References
        ---------

        """
        stack = ''
        last_indexes = {ch: i for i, ch in enumerate(s)}
        for i, ch in enumerate(s):
            if ch not in stack:
                while stack and stack[-1] > ch and i < last_indexes[stack[-1]]:
                    stack = stack[:-1]
                stack += ch
        return stack
