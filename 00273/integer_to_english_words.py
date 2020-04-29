

class Solution:
    def numberToWords(self, num: int) -> str:
        """
        ####  [273. Integer to English Words](https://leetcode.com/problems/integer-to-english-words/)

        Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

        **Example 1:**

        ```
        Input: 123
        Output: "One Hundred Twenty Three"
        ```

        **Example 2:**

        ```
        Input: 12345
        Output: "Twelve Thousand Three Hundred Forty Five"
        ```

        **Example 3:**

        ```
        Input: 1234567
        Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
        ```

        **Example 4:**

        ```
        Input: 1234567891
        Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
        ```

        Parameters
        ----------
        num: int

        Returns
        -------
        str

        Examples
        --------

        Notes
        -----

        References
        ---------

        """
        def words(n):
            to19 = 'One Two Three Four Five Six Seven Eight Nine Ten ' \
                   'Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split(' ')

            tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split(' ')

            if n < 20:
                return to19[n-1:n]

            if n < 100:
                return [tens[n//10-2]] + words(n % 10)

            if n < 1000:
                return [to19[n//100-1], 'Hundred'] + words(n % 100)

            for p, c in enumerate(['Thousand', 'Million', 'Billion'], 1):
                if n < 1000**(p+1):
                    return words(n//(1000**p)) + [c] + words(n % (1000**p))

        return ' '.join(words(num)) or 'Zero'

