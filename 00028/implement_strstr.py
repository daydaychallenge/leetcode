
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        #### [28. Implement strStr()](https://leetcode.com/problems/implement-strstr/)

        Implement [strStr()](http://www.cplusplus.com/reference/cstring/strstr/).

        Return the index of the first occurrence of needle in haystack, or **-1** if needle is not part of haystack.

        **Example 1:**

        ```
        Input: haystack = "hello", needle = "ll"
        Output: 2
        ```

        **Example 2:**

        ```
        Input: haystack = "aaaaa", needle = "bba"
        Output: -1
        ```

        **Clarification:**

        What should we return when `needle` is an empty string? This is a great question to ask during an interview.

        For the purpose of this problem, we will return 0 when `needle` is an empty string. This is consistent to C's [strstr()](http://www.cplusplus.com/reference/cstring/strstr/) and Java's [indexOf()](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html#indexOf(java.lang.String)).


        Parameters
        ----------
        haystack: str
        needle: str

        Returns
        -------
        int

        Examples
        --------

        Notes
        -----

        References
        ---------
        .. [1] https://blog.csdn.net/v_JULY_v/article/details/7041827

        """
        if not needle:
            return 0
        dp_next = [0 for _ in needle]
        dp_next[0], k, j = -1, -1, 0
        while j < len(needle)-1:
            if k == -1 or needle[k] == needle[j]:
                k, j = k + 1, j + 1
                dp_next[j] = k
            else:
                k = dp_next[k]
        i = j = 0
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                j = dp_next[j]
        if j == len(needle):
            return i-j
        return -1

    def strRabinKarp(self, haystack: str, needle: str) -> int:
        h, n = len(haystack), len(needle)
        if h < n:
            return -1

        def h2int(i):
            return ord(haystack[i]) - ord('a')

        def n2int(i):
            return ord(needle[i]) - ord('a')
        p, mod = 26, 10**9+7
        ref_hash = hay_hash = 0
        for i in range(n):
            ref_hash = (ref_hash*p + n2int(i)) % mod
            hay_hash = (hay_hash*p + h2int(i)) % mod

        if ref_hash == hay_hash:
            return 0
        hp = pow(p, n, mod)
        for i in range(1, h-n+1):
            hay_hash = (hay_hash*p - h2int(i-1)*hp + h2int(i+n-1)) % mod
            if hay_hash == ref_hash:
                return i
        return -1
