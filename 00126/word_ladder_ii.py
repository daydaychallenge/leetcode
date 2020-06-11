from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
        #### [126. Word Ladder II](https://leetcode.com/problems/word-ladder-ii/)

        Given two words (*beginWord* and *endWord*), and a dictionary's word list, find all shortest transformation sequence(s) from *beginWord* to *endWord*, such that:

        1. Only one letter can be changed at a time
        2. Each transformed word must exist in the word list. Note that *beginWord* is *not* a transformed word.

        **Note:**

        - Return an empty list if there is no such transformation sequence.
        - All words have the same length.
        - All words contain only lowercase alphabetic characters.
        - You may assume no duplicates in the word list.
        - You may assume *beginWord* and *endWord* are non-empty and are not the same.

        **Example 1:**

        ```
        Input:
        beginWord = "hit",
        endWord = "cog",
        wordList = ["hot","dot","dog","lot","log","cog"]

        Output:
        [
          ["hit","hot","dot","dog","cog"],
          ["hit","hot","lot","log","cog"]
        ]
        ```

        **Example 2:**

        ```
        Input:
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log"]

        Output: []

        Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
        ```


        Parameters
        ----------
        beginWord: str
        endWord: str
        wordList: List[str]

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
        words = set(wordList)
        if endWord not in words:
            return []
        chars = set(''.join(words))
        layer = {beginWord: [[beginWord]]}

        while layer:
            new_layer = defaultdict(list)
            for word in layer:
                if word == endWord:
                    return layer[word]
                for i in range(len(word)):
                    for c in chars:
                        next_word = word[:i] + c + word[i+1:]
                        if next_word in words:
                            new_layer[next_word] += [pre+[next_word] for pre in layer[word]]
            words -= set(new_layer.keys())
            layer = new_layer

        return []
