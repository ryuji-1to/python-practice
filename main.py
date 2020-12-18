from typing import List
import random
import hashlib


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


def binary_search(numbers: List[int], value: int) -> int:
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


def binary_search_2(numbers: List[int], value: int) -> int:
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


class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList(object):
    def __init__(self, head=None) -> None:
        self.head = head

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


class HashTable(object):
    def __init__(self, size=10) -> None:
        self.size = size
        self.table = [[] for i in range(self.size)]

    def hash(self, key) -> int:
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size

    def add(self, key, value) -> None:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                data[1] = value
                break
        else:
            self.table[index].append([key, value])

    def print(self) -> None:
        for index in range(self.size):
            print(index, end=" ")
            for data in self.table[index]:
                print("-->", end=" ")
                print(data, end=" ")

            print()

    def get(self, key):
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                return data[1]

    def __setitem__(self, key, value) -> None:
        self.add(key, value)

    def __getitem__(self, key):
        return self.get(key)


if __name__ == '__main__':
    hash_table = HashTable()
    hash_table["car"] = "Tesla"
    hash_table["pc"] = "Mac"
    hash_table["sns"] = "YouTube"
    # print(hash_table.table)
    hash_table.print()
    print(hash_table.get("sns"))
