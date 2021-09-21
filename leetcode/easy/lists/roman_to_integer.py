def romanToInt(s):
    d = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    special = ['I', 'X', 'C']

    nums = []

    for i, value in enumerate(s):
        if i != len(s) - 1:
            if s[i] in special and d[s[i]] < d[s[i+1]]:
                nums.append(-d[s[i]])
            else:
                nums.append(d[s[i]])
        else:
            nums.append(d[s[i]])
    return sum(nums)


assert romanToInt("MCMXCIV") == 1994, 'wrong'
assert romanToInt("LVIII") == 58, 'wrong'
assert romanToInt("IX") == 9, 'wrong'
assert romanToInt("IV") == 4, 'wrong'
assert romanToInt("III") == 3, 'wrong'
