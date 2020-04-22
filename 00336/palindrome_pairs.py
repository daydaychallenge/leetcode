from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """
        #### [336. Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs)

        Given a list of **unique** words, find all pairs of **distinct** indices `(i, j)` in the given list, so that the concatenation of the two words, i.e. `words[i] + words[j]` is a palindrome.

        **Example 1:**

        ```
        Input: ["abcd","dcba","lls","s","sssll"]
        Output: [[0,1],[1,0],[3,2],[2,4]]
        Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
        ```

        **Example 2:**

        ```
        Input: ["bat","tab","cat"]
        Output: [[0,1],[1,0]]
        Explanation: The palindromes are ["battab","tabbat"]
        ```

        Parameters
        ----------
        words: List[str]

        Returns
        -------
        List[List[int]]

        Examples
        --------
        >>> sol = Solution()
        >>> sol.palindromePairs(['abcd', 'dcba', 'lls', 's', 'sssll'])
        [[0,1],[1,0],[3,2],[2,4]]
        >>> sol.palindromePairs(['bat','tab','cat'])
        [[0,1],[1,0]]

        Notes
        -----

        References
        ---------

        """
        lookup = {w[::-1]: i for i, w in enumerate(words)}
        res = []
        for i, w in enumerate(words):
            for j in range(len(w)+1):
                prefix, postfix = w[:j], w[j:]
                if prefix in lookup and lookup[prefix] != i and postfix[::-1] == postfix:
                    res.append([i, lookup[prefix]])
                if j > 0 and postfix in lookup and lookup[postfix] != i and prefix[::-1] == prefix:
                    res.append([lookup[postfix], i])
        return res

