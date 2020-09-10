

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        """
        #### [925. Long Pressed Name](https://leetcode.com/problems/long-pressed-name/)

        Your friend is typing his `name` into a keyboard. Sometimes, when typing a character `c`, the key might get *long pressed*, and the character will be typed 1 or more times.

        You examine the `typed` characters of the keyboard. Return `True` if it is possible that it was your friends name, with some characters (possibly none) being long pressed.



        **Example 1:**

        ```
        Input: name = "alex", typed = "aaleex"
        Output: true
        Explanation: 'a' and 'e' in 'alex' were long pressed.
        ```

        **Example 2:**

        ```
        Input: name = "saeed", typed = "ssaaedd"
        Output: false
        Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
        ```

        **Example 3:**

        ```
        Input: name = "leelee", typed = "lleeelee"
        Output: true
        ```

        **Example 4:**

        ```
        Input: name = "laiden", typed = "laiden"
        Output: true
        Explanation: It's not necessary to long press any character.
        ```



        **Constraints:**

        - `1 <= name.length <= 1000`
        - `1 <= typed.length <= 1000`
        - The characters of `name` and `typed` are lowercase letters.

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
        from itertools import groupby
        g1 = [(ch, len(list(grp))) for ch, grp in groupby(name)]
        g2 = [(ch, len(list(grp))) for ch, grp in groupby(typed)]
        if len(g1) != len(g2):
            return False
        return all(a[0] == b[0] and a[1] <= b[1] for a, b in zip(g1, g2))
