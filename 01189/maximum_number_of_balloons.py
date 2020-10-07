

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """
        ### [1189. Maximum Number of Balloons](https://leetcode.com/problems/maximum-number-of-balloons/)

        Given a string `text`, you want to use the characters of `text` to form as many instances of the word **"balloon"** as possible.

        You can use each character in `text` **at most once**. Return the maximum number of instances that can be formed.



        **Example 1:**

        **![img](https://assets.leetcode.com/uploads/2019/09/05/1536_ex1_upd.JPG)**

        ```
        Input: text = "nlaebolko"
        Output: 1
        ```

        **Example 2:**

        **![img](https://assets.leetcode.com/uploads/2019/09/05/1536_ex2_upd.JPG)**

        ```
        Input: text = "loonbalxballpoon"
        Output: 2
        ```

        **Example 3:**

        ```
        Input: text = "leetcode"
        Output: 0
        ```



        **Constraints:**

        - `1 <= text.length <= 10^4`
        - `text` consists of lower case English letters only.

        Notes
        -----

        References
        ---------

        """
        return min(text.count(c)//"balloon".count(c) for c in "balon")
