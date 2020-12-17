from typing import List
import random


def bubble_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        for j in range(len_numbers - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


def linear_search(numbers: List[int], value: int) -> int:
    for i in range(len(numbers)):
        if numbers[i] == value:
            return i
    return -1


def binary_search(numbers: List[int], value: int) -> List[int]:
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return - 1


def binary_search_2(numbers: List[int], value: int) -> List[int]:
    def _binary_search(numbers: List[int], value: int, left: int, right: int) -> int:
        if left > right:
            return - 1

        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            return _binary_search(numbers, value, mid + 1, right)
        else:
            _binary_search(numbers, value, left, mid - 1)

    _binary_search(numbers, value, 0, len(numbers)-1)


if __name__ == '__main__':
    numbers = sorted([random.randint(1, 10) for i in range(10)])
    print(numbers)
    print(binary_search_2(numbers, 10))
