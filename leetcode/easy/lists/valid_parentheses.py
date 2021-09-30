def isValid(s):
    s = list(s)

    if len(s) == 0:
        return True

    opposite = {
        '(': ')',
        '{': '}',
        '[': ']',
    }

    for i, val in enumerate(s):
        if len(s) == 1 or i == len(s) - 1:
            return False
        if s[i + 1] == opposite.get(s[i]):
            del s[i + 1]
            del s[i]
            return isValid(s)


