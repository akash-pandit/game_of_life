import numpy as np
from time import sleep

field = np.zeros([10, 10])


def birth(arr, x: int, y: int) -> None:
    if (x or y) < 1:
        raise ValueError('Please provide a valid coordinate system')
    if arr[y-1, x-1] == 0:
        arr[y-1, x-1] = 1


def death(arr, x: int, y: int) -> None:
    if (x or y) < 1:
        raise ValueError('Please provide a valid coordinate system')
    if arr[y-1, x-1] == 1:
        arr[y-1, x-1] = 0


def flip_cell(arr, x: int, y: int) -> None:
    if arr[y-1, x-1] == 0:
        birth(arr, x, y)
    elif arr[y-1, x-1] == 1:
        death(arr, x, y)


def get_neighbors(arr, x, y):
    rows, cols = arr.shape
    left = max(x-2, 0)
    right = min(x+1, cols)
    top = max(y-2, 0)
    bottom = min(y+1, rows-1)
    neighbors = arr[top:bottom, left:right]

    return sum(neighbors.flatten()) - arr[y-1,x-1]


def step_time(arr):
    nxt = arr.copy()
    for row in range(len(arr)):
        # rows are y
        for col in range(len(arr)):
            # cols are x
            if arr[row, col]:
                if get_neighbors(arr, col+1, row+1) == 2 or get_neighbors(arr, col+1, row+1) == 3:
                    nxt[row, col] = 1
                else:
                    print(get_neighbors(arr, col+1, row+1), 'neighbors,', end=' ')
                    # print(f'killing cell ({col+1}, {row+1})')
                    nxt[row, col] = 0
            else:
                if get_neighbors(arr, col+1, row+1) == 3:
                    nxt[row, col] = 1
                else:
                    nxt[row, col] = 0
    return nxt


if __name__ == '__main__':
    flip_cell(field, 2, 1)
    flip_cell(field, 3, 2)
    flip_cell(field, 1, 3)
    flip_cell(field, 2, 3)
    flip_cell(field, 3, 3)

    print('ITERATION 1', '='*100)
    print(field)

    for i in range(20):
        field = step_time(field)
        print('ITERATION', i+2, '='*100)
        print(field)
        sleep(2)
