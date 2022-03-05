def reverseWords(s: str) -> str:
    s_list = s.split(' ')
    r = ''
    for i, word in enumerate(s_list):
        word_list = list(word)
        word_list.reverse()
        word_new = ''.join(word_list)
        r += word_new
        if i != len(s_list) - 1:
            r += ' '
    return r


# string = "Let's take LeetCode contest"
string = "God Ding"

print(reverseWords(string))
