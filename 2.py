from trie import Trie


class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not all(
            isinstance(s, str) for s in strings
        ):
            raise TypeError("Input must be a list of strings")
        if not strings:
            return ""

        for i, word in enumerate(strings):
            self.put(word, i)

        prefix = []
        current = self.root

        while len(current.children) == 1 and current.value is None:
            char = next(iter(current.children))
            prefix.append(char)
            current = current.children[char]

        return "".join(prefix)


if __name__ == "__main__":
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    trie = LongestCommonWord()
    strings = []
    assert trie.find_longest_common_word(strings) == ""

    print("✅ Усі перевірки пройдено успішно.")
