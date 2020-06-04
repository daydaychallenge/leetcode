
class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        #### [345. Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/)

        Write a function that takes a string as input and reverse only the vowels of a string.

        **Example 1:**

        ```
        Input: "hello"
        Output: "holle"
        ```

        **Example 2:**

        ```
        Input: "leetcode"
        Output: "leotcede"
        ```

        **Note:**
         The vowels does not include the letter "y".


        Parameters
        ----------
        s: str

        Returns
        -------
        str

        Examples
        --------

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.com/problems/reverse-vowels-of-a-string/discuss/81355/Beat-99.7-using-python-two-pointers

        """
        vowels, s = set('aeiouAEIOU'), list(s)
        left, right = 0, len(s)-1
        while left < right:

            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1

            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
        return ''.join(s)

