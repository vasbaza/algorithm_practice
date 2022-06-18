from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    result = ""
    letter_index = 0
    while True:
        for word_index in range(len(strs) - 1):
            try:
                letter_one = strs[word_index][letter_index]
                letter_two = strs[word_index + 1][letter_index]
                if letter_one != letter_two:
                    return result
            except IndexError:
                return result
        if len(strs[0]) < letter_index + 1:
            return result
        result += strs[0][letter_index:letter_index + 1]
        letter_index += 1


assert longestCommonPrefix(["fl", "flooow", "flooooight"]) == "fl", "Fail 1"
assert longestCommonPrefix(["flower", "flooow", "flooooight"]) == "flo", "Fail 2"
assert longestCommonPrefix(["flooower", "flooow", "flooooight"]) == "flooo", "Fail 2"
assert longestCommonPrefix(["", "flooow", "flooooight"]) == "", "Fail 3"
assert longestCommonPrefix([""]) == "", "Fail 4"
