def floodFill(image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
    directions = [
        (0, 1),
        (1, 0),
        (-1, 0),
        (0, -1)
    ]

    color_to_change = image[sr][sc]
    stack = [(sr, sc)]
    visited = set()

    while stack:
        x, y = stack.pop(-1)
        image[x][y] = newColor
        visited.add((x, y))

        for left, right in directions:
            if x + left >= 0 and y + right >= 0 and (x + left, y + right) not in visited:
                try:
                    if image[x + left][y + right] == color_to_change:
                        stack.append((x + left, y + right))
                except IndexError:
                    pass
    return image


board = [[1, 1, 1],
         [1, 1, 0],
         [1, 0, 1]]
coordinate_1 = 1
coordinate_2 = 1
newColor = 2

print(floodFill(board, coordinate_1, coordinate_2, newColor))
