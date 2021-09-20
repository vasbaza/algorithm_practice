def b_search(arr, item):
    arr.sort()
    start = 0
    end = len(arr) - 1
    mid_ind = int((start + end) / 2)

    for i in range(len(arr)):
        if item < arr[start] or item > arr[end]:
            return 'No such item in given array!'
        elif arr[mid_ind] == item:
            return mid_ind
        elif arr[end] == item:
            return end
        elif arr[mid_ind] < item:
            start = mid_ind
            mid_ind = int((start + end) / 2)
        elif arr[mid_ind] > item:
            end = mid_ind
            mid_ind = int((start + end) / 2)


print(b_search([1, 10, 15, 16], 1))
