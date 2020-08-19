
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        #### [1249. Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/)

        Given a string s of `'('` , `')'` and lowercase English characters.

        Your task is to remove the minimum number of parentheses ( `'('` or `')'`, in any positions ) so that the resulting *parentheses string* is valid and return **any** valid string.

        Formally, a *parentheses string* is valid if and only if:

        - It is the empty string, contains only lowercase characters, or
        - It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid strings, or
        - It can be written as `(A)`, where `A` is a valid string.



        **Example 1:**

        ```
        Input: s = "lee(t(c)o)de)"
        Output: "lee(t(c)o)de"
        Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
        ```

        **Example 2:**

        ```
        Input: s = "a)b(c)d"
        Output: "ab(c)d"
        ```

        **Example 3:**

        ```
        Input: s = "))(("
        Output: ""
        Explanation: An empty string is also valid.
        ```

        **Example 4:**

        ```
        Input: s = "(a(b(c)d)"
        Output: "a(b(c)d)"
        ```



        **Constraints:**

        - `1 <= s.length <= 10^5`
        - `s[i]` is one of `'('` , `')'` and lowercase English letters`.`

        Parameters
        ----------
        s: str

        Returns
        -------
        str

        Examples
        --------
        >>> sol = Solution()
        >>> sol.minRemoveToMakeValid('lee(t(c)o)de)')
        'lee(t(c)o)de'
        >>> sol.minRemoveToMakeValid('a)b(c)d')
        'ab(c)d'
        >>> sol.minRemoveToMakeValid('))((')
        ''

        Notes
        -----

        References
        ---------

        """
        opens, closes, s = 0, 0, list(s)
        slen = len(s)
        for i in range(slen):
            if s[i] == '(':
                opens += 1
            if s[i] == ')':
                closes += 1
            if closes > opens and s[i] == ')':
                closes -= 1
                s[i] = ''
        i = slen - 1
        while i >= 0 and opens > closes:
            if s[i] == '(':
                s[i] = ''
                opens -= 1
            i -= 1
        return ''.join(s)
