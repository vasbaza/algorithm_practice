# ToDo: без превращения в строку

def isPalindrome(x):
    if x < 0:
        return False
    if x == 0:
        return True
    x_c = x
    arr = []

    while x_c >= 1:
        arr.append(x_c % 10)
        x_c = x_c//10

    arr = list(map(str, arr))
    num = int(''.join(arr))

    return num == x


print(isPalindrome(0))