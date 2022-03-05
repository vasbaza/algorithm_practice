def reverseString(s: list[str]) -> None:
    s.reverse()


def reverseStringFast(s: list[str]) -> None:
    left_pointer = 0
    right_pointer = len(s) - 1
    while left_pointer <= right_pointer:
        s[left_pointer], s[right_pointer] = s[right_pointer], s[left_pointer]
        left_pointer += 1
        right_pointer -= 1


string = ["h", "e", "l", "l", "o"]

reverseStringFast(string)

print(string)
