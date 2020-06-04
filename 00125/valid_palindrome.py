
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        #### [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

        Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

        **Note:** For the purpose of this problem, we define empty string as valid palindrome.

        **Example 1:**

        ```
        Input: "A man, a plan, a canal: Panama"
        Output: true
        ```

        **Example 2:**

        ```
        Input: "race a car"
        Output: false
        ```

        Parameters
        ----------
        s: str

        Returns
        -------
        bool

        Examples
        --------

        Notes
        -----

        References
        ---------

        """
        left, right = 0, len(s)-1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left, right = left+1, right-1
        return True
