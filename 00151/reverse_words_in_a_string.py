
class Solution:
    def reverseWords(self, s: str) -> str:
        """
        #### [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)

        Given an input string, reverse the string word by word.

        **Example 1:**

        ```
        Input: "the sky is blue"
        Output: "blue is sky the"
        ```

        **Example 2:**

        ```
        Input: "  hello world!  "
        Output: "world! hello"
        Explanation: Your reversed string should not contain leading or trailing spaces.
        ```

        **Example 3:**

        ```
        Input: "a good   example"
        Output: "example good a"
        Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
        ```

        **Note:**

        - A word is defined as a sequence of non-space characters.
        - Input string may contain leading or trailing spaces. However, your  reversed string should not contain leading or trailing spaces.
        - You need to reduce multiple spaces between two words to a single space in the reversed string.


        **Follow up:**

        For C programmers, try to solve it *in-place* in *O*(1) extra space.

        Parameters
        ----------
        s: str

        Returns
        -------
        str

        Examples
        --------
        >>> sol = Solution()
        >>> sol.reverseWords('a good   example')
        'example good a'
        >>> sol.reverseWords('  hello world!  ')
        'world! hello'

        Notes
        -----

        References
        ---------

        """
        def trim_spaces(s):
            left, right = 0, len(s)-1

            while left <= right and s[left] == ' ':
                left += 1

            while left <= right and s[right] == ' ':
                right -= 1

            output = []
            while left <= right:
                if s[left] != ' ':
                    output.append(s[left])
                elif output[-1] != ' ':
                    output.append(' ')
                left += 1
            return output

        def reverse(l, start, end):
            while start < end:
                l[start], l[end] = l[end], l[start]
                start += 1
                end -= 1

        def reverse_word(l):
            start = end = 0
            n = len(l)
            while start < n:
                while end < n and l[end] != ' ':
                    end += 1
                reverse(l, start, end-1)
                end += 1
                start = end

        l = trim_spaces(s)
        reverse(l, 0, len(l)-1)
        reverse_word(l)
        return ''.join(l)

    def reverseWordsV01(self, s: str) -> str:
        from collections import deque
        d, word = deque(), []
        left, right = 0, len(s)-1

        while left <= right and s[left] == ' ':
            left += 1

        while left <= right and s[right] == ' ':
            right -= 1

        while left <= right:
            if s[left] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        d.appendleft(''.join(word))

        return ' '.join(d)
