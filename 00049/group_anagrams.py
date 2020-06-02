from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        #### [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)

        Given an array of strings, group anagrams together.

        **Example:**

        ```
        Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
        Output:
        [
          ["ate","eat","tea"],
          ["nat","tan"],
          ["bat"]
        ]
        ```

        **Note:**

        - All inputs will be in lowercase.
        - The order of your output does not matter.

        Parameters
        ----------
        strs: str

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
        d = defaultdict(list)
        for w in strs:
            d[tuple(sorted(w))].append(w)
        return list(d.values())
