bad_version = 15

versions = 20


def is_bad_version(n):
    return n >= bad_version


def first_bad_version(n: int) -> int:
    start = 1
    end = n
    while start <= end:
        mid = (start + end) // 2
        if is_bad_version(mid):
            if end == mid or not is_bad_version(mid - 1):
                return mid
            else:
                end = mid - 1
        else:
            start = mid + 1


print(first_bad_version(versions))
