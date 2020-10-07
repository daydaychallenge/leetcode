class Codec:
    """
    ### [271. Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/)

    Design an algorithm to encode **a list of strings** to **a string**. The encoded string is then sent over the network and is decoded back to the original list of strings.

    Machine 1 (sender) has the function:

    ```
    string encode(vector<string> strs) {
      // ... your code
      return encoded_string;
    }
    ```

    Machine 2 (receiver) has the function:

    ```
    vector<string> decode(string s) {
      //... your code
      return strs;
    }
    ```

    So Machine 1 does:

    ```
    string encoded_string = encode(strs);
    ```

    and Machine 2 does:

    ```
    vector<string> strs2 = decode(encoded_string);
    ```

    `strs2` in Machine 2 should be the same as `strs` in Machine 1.

    Implement the `encode` and `decode` methods.



    **Note:**

    - The string may contain any possible characters out of 256 valid  ascii characters. Your algorithm should be generalized enough to work on any possible characters.
    - Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
    - Do not rely on any library method such as `eval` or serialize methods. You should implement your own encode/decode algorithm.


    """
    def encode(self, strs: [str]) -> str:
        def get_len_str(x: str):
            x = len(x)
            byte_list = [chr(x >> (i*8) & 0xff) for i in range(4)]
            byte_list.reverse()
            return ''.join(byte_list)
        ret = ''
        for s in strs:
            ret += get_len_str(s)
            ret += s
        return ret

    def decode(self, s: str) -> [str]:
        def str_to_len(bytes):
            result = 0
            for ch in bytes:
                result = result*256 + ord(ch)
            return result

        ret = []
        i, n = 0, len(s)
        while i < n:
            length = str_to_len(s[i:i+4])
            i += 4
            ret.append(s[i:i+length])
            i += length
        return ret




