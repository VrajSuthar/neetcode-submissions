from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        # Encoding
        for word in strs:
            for ch in word:
                encoded_str += str(ord(ch)) + "-"

            encoded_str += "#"

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_list = []

        # Split words
        words = s.split("#")

        # Ignore last empty split after final '#'
        for word in words[:-1]:

            letters = word.split("-")

            decoded_word = ""

            for n in letters:
                if n != "":
                    decoded_word += chr(int(n))

            decoded_list.append(decoded_word)

        return decoded_list
