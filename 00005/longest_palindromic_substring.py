
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        #### [5.Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

        Given a string **s**, find the longest palindromic substring in **s**. You may assume that the maximum length of **s** is 1000.

        **Example 1:**

        ```
        Input: "babad"
        Output: "bab"
        Note: "aba" is also a valid answer.
        ```

        **Example 2:**

        ```
        Input: "cbbd"
        Output: "bb"
        ```

        Parameters
        ----------
        s: str

        Returns
        -------
        str

        Examples
        --------
        >>> sol = Solution()
        >>> sol.longestPalindrome('babad')
        'bab'
        >>> sol.longestPalindrome('cbbd')
        'bb'

        Notes
        -----

        References
        ---------

        """
        s = '#' + '#'.join(s) + '#'
        s_len = len(s)
        r = [0 for _ in range(s_len)]
        pos = max_right = 0
        max_s = ''
        for i, c in enumerate(s):
            if i < max_right:
                r[i] = min(max_right-i, r[2*pos-i])
            else:
                r[i] = 1
            while i-r[i] >= 0 and i+r[i] < s_len and s[i-r[i]] == s[i+r[i]]:
                r[i] += 1
            if i+r[i] > max_right:
                max_right = i+r[i]
                pos = i
            if 2*r[i]-1 > len(max_s):
                max_s = s[i-r[i]+1:i+r[i]]
        return ''.join(max_s.split('#'))

    def longestPalindromeV01(self, s: str) -> str:
        n = len(s)

        def get_len(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return r-l-1

        start, length = 0, 0
        for i in range(n):
            cur = max(get_len(i, i), get_len(i, i+1))
            if cur <= length: continue
            length = cur
            start = i - (cur-1)//2
        return s[start: start+length]

