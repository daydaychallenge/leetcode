from typing import List


class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        """
        #### [758. Bold Words in String](https://leetcode.com/problems/bold-words-in-string/)

        Given a set of keywords `words` and a string `S`, make all appearances of all keywords in `S` bold. Any letters between `<b>` and `</b>` tags become bold.

        The returned string should use the least number of tags possible, and of course the tags should form a valid combination.

        For example, given that `words = ["ab", "bc"]` and `S = "aabcd"`, we should return `"a<b>abc</b>d"`. Note that returning `"a<b>a<b>b</b>c</b>d"` would use more tags, so it is incorrect.

        **Constraints:**

        - `words` has length in range `[0, 50]`.
        - `words[i]` has length in range `[1, 10]`.
        - `S` has length in range `[0, 500]`.
        - All characters in `words[i]` and `S` are lowercase letters.

        **Note:** This question is the same as 616: https://leetcode.com/problems/add-bold-tag-in-string/



        Parameters
        ----------
        words: List[str]
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
        from itertools import groupby
        n = len(S)
        mask = [False]*n
        for i in range(n):
            prefix = S[i:]
            for w in words:
                if prefix.startswith(w):
                    min_len = min(i+len(w), n)
                    mask[i:min_len] = [True]*(min_len-i)
        ans = []
        for inc, grp in groupby(zip(S, mask), lambda x: x[1]):
            if inc:
                ans.append('<b>')
            ans.append(''.join(x[0] for x in grp))
            if inc:
                ans.append('</b>')
        return ''.join(ans)
