from typing import List, Tuple, Optional, Iterator, Generator
from collections import deque
import random
import hashlib
import operator
import time
from collections import Counter
import operator
from itertools import permutations


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


def getPair(numbers: List[int], target: int) -> Optional[Tuple[int, int]]:
    cache = set()
    for num in numbers:
        val = target - num
        if val in cache:
            return val, num
        cache.add(num)


def getPair_half_sum(numbers: List[int]) -> Optional[Tuple[int, int]]:
    sum_numbers = sum(numbers)
    # if sum_numbers % 2 != 0:
    #     return
    # half_sum = int(sum_numbers / 2)
    half_sum, remainder = divmod(sum_numbers, 2)
    if remainder != 0:
        return
    cache = set()
    for num in numbers:
        cache.add(num)
        val = half_sum - num
        if val in cache:
            return val, num


class Stack(object):

    def __init__(self) -> None:
        self.stack = []

    def push(self, data) -> None:
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()


def validate_format(chars: str) -> bool:
    lookup = {"{": "}", "[": "]", "(": ")"}
    stack = []
    for c in chars:
        if c in lookup.keys():
            stack.append(lookup[c])
        if c in lookup.values():
            if not stack:
                return False
            if c != stack.pop():
                return False
    if stack:
        return False
    return True


class Que(object):

    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)


def reverse(queue):
    new_queue = deque()
    while queue:
        new_queue.append(queue.pop())

    return new_queue


class Node(object):
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


def insert(node: Node, value: int) -> Node:
    if node is None:
        return Node(value)
    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node


def find_pair(pairs: List[Tuple[int, int]]) -> Iterator[Tuple[int, int]]:
    cache = {}
    for pair in pairs:
        first, second = pair[0], pair[1]
        value = cache.get(second)
        if not value:
            cache[first] = second
        elif value == first:
            yield pair


def find_max_value(value: str):
    cache = []
    for a in value:
        if a.isalpha():
            cache.append(a.lower())
    List = Counter(cache).most_common()
    print(cache)
    return List[0]


def count_chars_v1(strings: str) -> Tuple[str, int]:
    strings = strings.lower()
    # l = []
    # for char in strings:
    #     if not char.isspace():
    #         l.append((char, strings.count(char)))
    l = [(c, strings.count(c)) for c in strings if not c.isspace()]
    return max(l, key=operator.itemgetter(1))


def count_chars_v2(strings: str) -> Tuple[str, int]:
    strings = strings.lower()
    d = {}
    for char in strings:
        if not char.isspace():
            d[char] = d.get(char, 0) + 1
    max_key = max(d, key=d.get)
    return max_key, d[max_key]


def count_chars_v3(strings: str) -> Tuple[str, int]:
    strings = strings.lower()
    d = Counter()
    for char in strings:
        print(d)
        if not char.isspace():
            d[char] += 1
    max_key = max(d, key=d.get)
    print(d)
    return max_key, d[max_key]


def memoize(f):
    cache = {}

    def _wrapper(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return _wrapper


# @memoize
def long_func(num: int) -> int:
    r = 0
    for i in range(10000000):
        r += num * i
    return r


def min_count_remove(x: List[int], y: List[int]) -> None:
    # count_x = {}
    # count_y = {}
    # for i in x:
    #     count_x[i] = count_x.get(i, 0) + 1
    # for i in y:
    #     count_y[i] = count_y.get(i, 0) + 1
    counter_x = Counter(x)
    counter_y = Counter(y)

    for key_x, value_x in counter_x.items():
        value_y = counter_y.get(key_x)
        if value_y:
            if value_x < value_y:
                x[:] = [i for i in x if i != key_x]
            elif value_x > value_y:
                y[:] = [i for i in y if i != key_x]


def remove_zero(numbers: List[int]) -> None:
    if numbers and numbers[0] == 0:
        numbers.pop(0)
        remove_zero(numbers)


def list_to_int(numbers: List[int]) -> int:
    sum_numbers = 0
    for i, num in enumerate(reversed(numbers)):
        sum_numbers += num * (10 ** i)
    return sum_numbers


def list_to_int_plus_one(numbers: List[int]) -> int:
    i = len(numbers) - 1
    numbers[i] += 1
    while 0 < i:
        if numbers[i] != 10:
            remove_zero(numbers)
            break

        numbers[i] = 0
        numbers[i-1] += 1
        i -= 1
    else:
        if numbers[0] == 10:
            numbers[0] = 1
            numbers.append(0)
    return list_to_int(numbers)


def snake_string_v1(chars: str) -> List[List[str]]:
    result = [[], [], []]
    result_indexes = {0, 1, 2}
    insert_index = 1
    for i, s in enumerate(chars):
        if i % 4 == 1:
            insert_index = 0
        elif i % 2 == 0:
            insert_index = 1
        elif i % 4 == 3:
            insert_index = 2
        result[insert_index].append(s)
        for rest_index in result_indexes - {insert_index}:
            result[rest_index].append(" ")
    return result


def snake_string_v2(chars: str, depth: int) -> List[List[str]]:
    result = [[] for _ in range(depth)]
    result_indexes = {i for i in range(depth)}
    insert_index = int(depth / 2)

    # def pos(i):
    #     return i + 1

    # def neg(i):
    #     return i - 1
    op = operator.neg

    for s in chars:
        result[insert_index].append(s)
        for rest_index in result_indexes - {insert_index}:
            result[rest_index].append(" ")
        if insert_index <= 0:
            op = operator.pos
        if insert_index >= depth - 1:
            op = operator.neg
        insert_index += op(1)
    return result


def get_max_sequence_sum(numbers: List[int]) -> int:
    result_sequence, sum_sequence = 0, 0
    for num in numbers:
        # temp_sum_sequence = sum_sequence + num
        # if num < temp_sum_sequence:
        #     sum_sequence = temp_sum_sequence
        # else:
        #     sum_sequence = num
        sum_sequence = max(num, sum_sequence + num)

        # if result_sequence < sum_sequence:
        #     result_sequence = sum_sequence
        result_sequence = max(result_sequence, sum_sequence)
    return result_sequence


def find_max_circular_sequence(numbers: List[int]) -> int:
    max_sequence_sum = get_max_sequence_sum(numbers)
    invert_numbers = []
    all_sum = 0
    for num in numbers:
        all_sum += num
        invert_numbers.append(-num)
    max_wrap_sequence = all_sum-(-get_max_sequence_sum(invert_numbers))
    return max(max_sequence_sum, max_wrap_sequence)


def delete_duplicate_v1(numbers: List[int]) -> None:
    tmp = []
    for num in numbers:
        if num not in tmp:
            tmp.append(num)
    numbers[:] = tmp
    print(numbers)


def delete_duplicate_v2(numbers: List[int]) -> None:
    tmp = [numbers[0]]
    i, len_num = 0, len(numbers) - 1
    while i < len_num:
        if numbers[i] != numbers[i + 1]:
            tmp.append(numbers[i + 1])
        i += 1
    numbers[:] = tmp
    print(numbers)


def delete_duplicate_v3(numbers: List[int]) -> None:
    i, len_numbers = 0, len(numbers) - 1
    while i < len(numbers)-1:
        if numbers[i] == numbers[i + 1]:
            numbers.remove((numbers[i]))
            i -= 1
        i += 1


def delete_duplicate_v4(numbers: List[int]) -> None:
    i = len(numbers) - 1
    while i > 0:
        if numbers[i] == numbers[i - 1]:
            numbers.pop(i)
        i -= 1


def all_perms(elements: List[int]) -> Iterator[List[int]]:

    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


def is_palindrome(strings: str) -> bool:
    len_strings = len(strings)
    if not len_strings:
        return False
    if len_strings == 1:
        return True
    start, end = 0, len_strings-1
    while start < end:
        if strings[start] != strings[end]:
            return False
        start += 1
        end -= 1
    return True


def find_palindrome(strings: str, left: int, right: int):
    # result = []
    while 0 <= left and right <= len(strings) - 1:
        if strings[left] != strings[right]:
            break
        yield strings[left: right + 1]
        left -= 1
        right += 1


def find__all_palindrome(strings: str):
    # result = []
    len_strings = len(strings)
    if not len_strings:
        yield
    if len_strings == 1:
        yield strings

    for i in range(1, len_strings - 1):
        yield from find_palindrome(strings, i - 1, i + 1)
        yield from find_palindrome(strings, i - 1, i)


if __name__ == '__main__':
    s = []
    [s.append(i) for i in range(10)]
    print(s)
