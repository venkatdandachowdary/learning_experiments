import functools
from operator import add


def largest_element(list_):
    """
    1 Write a function that returns the largest element in a list.
    """
    largest_elem = list_[0]
    for elem in list_[1:]:
        if len(elem) > len(largest_elem):
            largest_elem = elem

    return largest_elem


def reverse_in_place(list_):
    """
    2 Write function that reverses a list, preferably in place.
    """
    return list(reversed(list_))


def item_is_in_list(item, list_):
    """
    3 Write a function that checks whether an element occurs in a list.
    """
    return item in list_


def odd_elements(list_):
    """
    4 Write a function that returns the elements on odd positions in a list.
    """
    return list_[::2]


def running_total(list_):
    """
    5 Write a function that computes the running total of a list.
    """
    return functools.reduce(add, list_)


def is_palindrome(string_):
    """
    6 Write a function that tests whether a string is a palindrome.
    """
    backwards_string = "".join(reversed(string_))
    return string_ == backwards_string


def for_sum(numbers):
    """
    7 Write three functions that compute the sum of the numbers in a list: using a for-loop, a while-loop and recursion.
    (Subject to availability of these constructs in your language of choice.)
    """
    total = 0
    for number in numbers:
        total += number

    return total


def while_sum(numbers):
    """
    """
    total = 0
    i = 0
    while i < len(numbers):
        total += numbers[i]
        i += 1

    return total


def recursive_sum(numbers):
    """
    """
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + recursive_sum(numbers[1:])


def on_all(func, list_):
    """
    8 Write a function on_all that applies a function to every element of a list. Use it to print the first twenty perfect squares.
    """
    mapped_list = []
    for elem in list_:
        mapped_list.append(func(elem))

    return mapped_list


def square(x):
    return x * x

if __name__ == "__main__":
    print("The first 20 perfect squares are:")
    first_twenty_numbers = range(1, 21)
    first_twenty_squares = on_all(square, range(1,21))

    print("\n".join(["{}={}".format(str(x), str(sq)) for x, sq in zip(first_twenty_numbers, first_twenty_squares)]))


def concat_lists(*lists):
    """
    9 Write a function that concatenates two lists.
    """
    mega_list = []
    for list_ in lists:
        mega_list.extend(list_)

    return mega_list


def alternate_combine(*lists):
    """
    10 Write a function that combines two lists by alternatingly taking elements, e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].
    """
    new_list = []
    for elems in zip(*lists):
        print(elems)
        new_list.extend(elems)

    return new_list


def merge_sorted_lists(list1, list2):
    """
    11 Write a function that merges two sorted lists into a new list.
    """
    return []


def rotate_list(list_, k):
    """
    12 Write a function that rotates a list by k elements.
    For example [1,2,3,4,5,6] rotated by two becomes [3,4,5,6,1,2].
    Try solving this without creating a copy of the list.
    How many swap or move operations do you need?
    """
    return list_[k:] + list_[:k]


def find_fibonacci_numbers(n):
    """
    13 Write a function that computes the list of the first 100 Fibonacci numbers.
    """
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


def number_to_digits(num):
    """
    14 Write a function that takes a number and returns a list of its digits.
    """
    return [int(ch) for ch in str(num)]


# 15 Write functions that add, subtract, and multiply two numbers in their digit-list representation
# and return a new digit list).
# If you’re ambitious you can implement Karatsuba multiplication.
# Try different bases. What is the best base if you care about speed?
# If you couldn’t completely solve the prime number exercise above due to the lack of large numbers in your language,
# you can now use your own library for this task.


# 16 Implement the following sorting algorithms:
# Selection sort,
# Insertion sort,
# Merge sort,
# Quick sort,
# Stooge Sort.
# Check Wikipedia for descriptions.
def my_selection_sort(list):
    sorted_list = []
    return sorted_list


def my_insertion_sort(list):
    sorted_list = []
    return sorted_list


def my_merge_sort(list):
    sorted_list = []
    return sorted_list


def my_quick_sort(list):
    sorted_list = []
    return sorted_list


def my_stooge_sort(list):
    sorted_list = []
    return sorted_list


def my_binary_search(list, find):
    # 17 Implement binary search.
    position = None

    if position == None:
        raise ValueError("Value Not Found")
    return position


def boxify(list_of_strings):
    """
    18 Write a function that takes a list of strings an prints them, one per line,
    in a rectangular frame. For example the list
    ["Hello", "World", "in", "a", "frame"] gets printed as:

    *********
    * Hello *
    * World *
    * in    *
    * a     *
    * frame *
    *********
    """
    longest_len = 0
    for string_ in list_of_strings:
        if len(string_) > longest_len:
            longest_len = len(string_)

    line_width = longest_len + 4
    boxed_lines = [
        "*" * line_width
    ]
    for line in list_of_strings:
        spaces = longest_len - len(line)
        boxed_lines.append(
            "* {}{} *".format(line, ' '*spaces)
        )
    boxed_lines.append("*" * line_width)
    return boxed_lines


if __name__ == "__main__":
    lines = ["Hello", "World", "in", "a", "frame"]
    for line in boxify(lines):
        print(line)


def pig_latinify(text):
    """
    19 Write function that translates a text to Pig Latin and back.
    English is translated to Pig Latin by taking the first letter of every word, moving it to the end of
    the word and adding ‘ay’. “The quick brown fox” becomes “Hetay uickqay rownbay oxfay”.
    """
    words = text.split(' ')
    pl_words = []
    for word in words:
        pl_words.append(
            "{}{}ay".format(word[1:].lower(), word[0].lower())
        )

    # capitalise the first word

    pl_words[0] = pl_words[0][0].upper() + pl_words[0][1:]
    return " ".join(pl_words)
