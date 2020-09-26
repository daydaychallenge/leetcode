

class Solution:
    def isValid(self, code: str) -> bool:
        """
        ### [591. Tag Validator](https://leetcode.com/problems/tag-validator/)

        Given a string representing a code snippet, you need to implement a tag validator to parse the code and return whether it is valid. A code snippet is valid if all the following rules hold:


        1. The code must be wrapped in a **valid closed tag**. Otherwise, the code is invalid.
        2. A **closed tag** (not necessarily valid) has exactly the following format : `<TAG_NAME>TAG_CONTENT</TAG_NAME>`. Among them, `<TAG_NAME>` is the start tag, and `</TAG_NAME>` is the end tag. The TAG_NAME in start and end tags should be the same. A closed tag is **valid** if and only if the TAG_NAME and TAG_CONTENT are valid.
        3. A **valid** `TAG_NAME` only contain **upper-case letters**, and has length in range [1,9]. Otherwise, the `TAG_NAME` is **invalid**.
        4. A **valid** `TAG_CONTENT` may contain other **valid closed tags**, **cdata** and any characters (see note1) **EXCEPT** unmatched `<`, unmatched start and end tag, and unmatched or closed tags with invalid TAG_NAME. Otherwise, the `TAG_CONTENT` is **invalid**.
        5. A start tag is unmatched if no end tag exists with the same TAG_NAME, and vice versa. However, you also need to consider the issue of unbalanced when tags are nested.
        6. A `<` is unmatched if you cannot find a subsequent `>`. And when you find a `<` or `</`, all the subsequent characters until the next `>` should be parsed as TAG_NAME (not necessarily valid).
        7. The cdata has the following format : `<![CDATA[CDATA_CONTENT]]>`. The range of `CDATA_CONTENT` is defined as the characters between `<![CDATA[` and the **first subsequent** `]]>`.
        8. `CDATA_CONTENT` may contain **any characters**. The function of cdata is to forbid the validator to parse `CDATA_CONTENT`, so even it has some characters that can be parsed as tag (no matter valid or invalid), you should treat it as **regular characters**.

        **Valid Code Examples:**

        ```
        Input: "<DIV>This is the first line <![CDATA[<div>]]></DIV>"

        Output: True

        Explanation:

        The code is wrapped in a closed tag : <DIV> and </DIV>.

        The TAG_NAME is valid, the TAG_CONTENT consists of some characters and cdata.

        Although CDATA_CONTENT has unmatched start tag with invalid TAG_NAME, it should be considered as plain text, not parsed as tag.

        So TAG_CONTENT is valid, and then the code is valid. Thus return true.


        Input: "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"

        Output: True

        Explanation:

        We first separate the code into : start_tag|tag_content|end_tag.

        start_tag -> "<DIV>"

        end_tag -> "</DIV>"

        tag_content could also be separated into : text1|cdata|text2.

        text1 -> ">>  ![cdata[]] "

        cdata -> "<![CDATA[<div>]>]]>", where the CDATA_CONTENT is "<div>]>"

        text2 -> "]]>>]"


        The reason why start_tag is NOT "<DIV>>>" is because of the rule 6.
        The reason why cdata is NOT "<![CDATA[<div>]>]]>]]>" is because of the rule 7.
        ```



        **Invalid Code Examples:**

        ```
        Input: "<A>  <B> </A>   </B>"
        Output: False
        Explanation: Unbalanced. If "<A>" is closed, then "<B>" must be unmatched, and vice versa.

        Input: "<DIV>  div tag is not closed  <DIV>"
        Output: False

        Input: "<DIV>  unmatched <  </DIV>"
        Output: False

        Input: "<DIV> closed tags with invalid tag name  <b>123</b> </DIV>"
        Output: False

        Input: "<DIV> unmatched tags with invalid tag name  </1234567890> and <CDATA[[]]>  </DIV>"
        Output: False

        Input: "<DIV>  unmatched start tag <B>  and unmatched end tag </C>  </DIV>"
        Output: False
        ```



        **Note:**

        1. For simplicity, you could assume the input code (including the **any characters** mentioned above) only contain `letters`, `digits`, `'<'`,`'>'`,`'/'`,`'!'`,`'['`,`']'` and `' '`.

        Parameters
        ----------
        version1: str
        version2: str

        Returns
        -------
        int

        Examples
        --------
        >>> sol = Solution()
        >>> sol.isValid('<DIV>This is the first line <![CDATA[<div>]]></DIV>')
        True
        >>> sol.isValid('<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>')
        True

        Notes
        -----

        References
        ---------

        """
        def collect_tag(s):
            i = 0
            while i < len(s):
                if s[i] == '>':
                    return s[:i]
                i += 1
            return None

        def valid_tag(t: str) -> bool:
            return 1 <= len(t) <= 9 and all('A' <= c <= 'Z' for c in t)

        if not code or not code[0] == '<':
            return False

        tag = collect_tag(code[1:])
        if not tag or not valid_tag(tag) or not code.startswith(f'<{tag}>') or not code.endswith(f'</{tag}>'):
            return False

        stack, i = [], 0
        code = code[len(tag)+2:-len(tag)-3]
        begin_data, end_data = '![CDATA[', ']]>'
        while i < len(code):
            if code[i] == '<':
                tag = collect_tag(code[i+1:])
                if not tag:
                    return False
                if tag.startswith(begin_data):
                    while i < len(code) and code[i:i+3] != end_data:
                        i += 1
                    if code[i:i+3] != end_data:
                        return False
                    i += 2
                elif tag.startswith('/'):
                    tag = tag[1:]
                    if not valid_tag(tag) or not stack or stack.pop() != tag:
                        return False
                else:
                    if not valid_tag(tag):
                        return False
                    stack.append(tag)

            i += 1

        return not stack
