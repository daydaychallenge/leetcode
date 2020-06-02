from typing import List
from collections import deque, defaultdict, Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        #### [30. Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)

        You are given a string, **s**, and a list of words, **words**, that are all of the same length. Find all starting indices of substring(s) in **s** that is a concatenation of each word in **words** exactly once and without any intervening characters.


        **Example 1:**

        ```
        Input:
          s = "barfoothefoobarman",
          words = ["foo","bar"]
        Output: [0,9]
        Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
        The output order does not matter, returning [9,0] is fine too.
        ```

        **Example 2:**

        ```
        Input:
          s = "wordgoodgoodgoodbestword",
          words = ["word","good","best","word"]
        Output: []
        ```

        Parameters
        ----------
        s: str
        words: List[str]

        Returns
        -------
        List[int]

        Examples
        --------

        Notes
        -----

        References
        ---------
        .. [1] https://leetcode.wang/leetCode-30-Substring-with-Concatenation-of-All-Words.html
        .. [2] https://leetcode.com/problems/substring-with-concatenation-of-all-words/discuss/13668/Python-Solution-K-Sliding-Window

        """
        if not words:
            return []
        res, word_len, counts = [], len(words[0]), Counter(words)
        total, foot_print = word_len * len(words), defaultdict(deque)
        for start in range(word_len):
            end = start
            foot_print.clear()
            while start + total <= len(s):
                word = s[end:end+word_len]
                end += word_len
                if word in counts:
                    queue = foot_print[word]
                    queue.append(end)
                    while queue[0] < start:
                        queue.popleft()
                    if len(queue) > counts[word]:
                        start = queue.popleft()
                    if start + total == end:
                        res.append(start)
                else:
                    start = end
        return res

