from typing import List


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        """
        ### [916. Word Subsets](https://leetcode.com/problems/word-subsets/)

        We are given two arrays `A` and `B` of words. Each word is a string of lowercase letters.

        Now, say that word `b` is a subset of word `a` if every letter in `b` occurs in `a`, **including multiplicity**. For example, `"wrr"` is a subset of `"warrior"`, but is not a subset of `"world"`.

        Now say a word `a` from `A` is *universal* if for every `b` in `B`, `b` is a subset of `a`.

        Return a list of all universal words in `A`. You can return the words in any order.

        **Example 1:**

        ```
        Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
        Output: ["facebook","google","leetcode"]
        ```

        **Example 2:**

        ```
        Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
        Output: ["apple","google","leetcode"]
        ```

        **Example 3:**

        ```
        Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
        Output: ["facebook","google"]
        ```

        **Example 4:**

        ```
        Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
        Output: ["google","leetcode"]
        ```

        **Example 5:**

        ```
        Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
        Output: ["facebook","leetcode"]
        ```



        **Note:**

        1. `1 <= A.length, B.length <= 10000`
        2. `1 <= A[i].length, B[i].length <= 10`
        3. `A[i]` and `B[i]` consist only of lowercase letters.
        4. All words in `A[i]` are unique: there isn't `i != j` with `A[i] == A[j]`.


        Notes
        -----

        References
        ---------

        """
        def count(word):
            letters = [0]*26
            for ch in word:
                letters[ord(ch)-ord('a')] += 1
            return letters

        bmax = [0]*26
        for word in B:
            for i, val in enumerate(count(word)):
                bmax[i] = max(bmax[i], val)

        ans = []
        for word in A:
            if all(a >= b for a, b in zip(count(word), bmax)):
                ans.append(word)

        return ans


