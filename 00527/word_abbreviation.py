from typing import List


class Solution:
    def wordsAbbreviation(self, dicts: List[str]) -> List[str]:
        """
        ### [527. Word Abbreviation](https://leetcode.com/problems/word-abbreviation/)

        Given an array of n distinct non-empty strings, you need to generate **minimal** possible abbreviations for every word following rules below.

        1. Begin with the first character and then the number of characters abbreviated, which followed by the last character.
        2. If there are any conflict, that is more than one words share the  same abbreviation, a longer prefix is used instead of only the first  character until making the map from word to abbreviation become unique.  In other words, a final abbreviation cannot map to more than one  original words.
        3.  If the abbreviation doesn't make the word shorter, then keep it as original.

        **Example:**

        ```
        Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
        Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
        ```


        **Note:**

        1.  Both n and the length of each word will not exceed 400.
        2.  The length of each word is greater than 1.
        3.  The words consist of lowercase English letters only.
        4.  The return answers should be **in the same order** as the original array.

        Notes
        -----

        References
        ---------

        """
        def longest_prefix(w1, w2):
            pi = 0
            while pi < len(w1) and pi < len(w2) and w1[pi] == w2[pi]:
                pi += 1
            return pi

        from collections import defaultdict
        groups = defaultdict(list)
        for i, w in enumerate(dicts):
            groups[(len(w), w[0], w[-1])].append((w, i))
        ans = [None for _ in dicts]
        for (size, first, last), enum_words in groups.items():
            enum_words.sort()
            lcp = [0]*len(enum_words)
            for i, (word, _) in enumerate(enum_words):
                if i:
                    word1 = enum_words[i-1][0]
                    lcp[i] = longest_prefix(word1, word)
                    lcp[i-1] = max(lcp[i-1], lcp[i])

            for (word, index), p in zip(enum_words, lcp):
                delta = size - p - 2
                if delta <= 1:
                    ans[index] = word
                else:
                    ans[index] = word[:p+1] + str(delta) + word[-1]
        return ans




