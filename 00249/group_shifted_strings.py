from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        """
        #### [249. Group Shifted Strings](https://leetcode.com/problems/group-shifted-strings/)

        Given a string, we can "shift" each of its letter to its successive letter, for example: `"abc" -> "bcd"`. We can keep "shifting" which forms the sequence:

        ```
        "abc" -> "bcd" -> ... -> "xyz"
        ```

        Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

        **Example:**

        ```
        Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
        Output:
        [
          ["abc","bcd","xyz"],
          ["az","ba"],
          ["acef"],
          ["a","z"]
        ]
        ```

        Parameters
        ----------
        strings: List[str]

        Returns
        -------
        List[List[str]]

        Examples
        --------

        Notes
        -----

        References
        ---------

        """
        from collections import defaultdict
        groups = defaultdict(list)
        for s in strings:
            groups[tuple((ord(c)-ord(s[0])) % 26 for c in s)].append(s)
        return list(groups.values())
