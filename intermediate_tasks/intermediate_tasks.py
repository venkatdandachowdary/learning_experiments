import itertools


# 1 Write a program that outputs all possibilities to put + or - or
# nothing between the numbers 1,2,...,9 (in this order) such that the
# result is 100. For example 1 + 2 + 3 - 4 + 5 + 6 + 78 + 9 = 100.
def interleave(operators, numbers):
    if len(numbers) != len(operators) + 1:
        raise ValueError('Not enough operators for the supplied numbers')

    interleaved_list = []
    for i in range(0, len(numbers)):
        interleaved_list.append(numbers[i])
        if i < len(operators):
            interleaved_list.append(operators[i])

    # remove the spaces
    return [x for x in interleaved_list if x != ' ']


def do_sum(numbers, operators):
    # do the sum. eval is perhaps a little hacky, but hey ;)
    return int(eval(create_sum_string(numbers, operators)))


def create_sum_string(numbers, operators):
    interleaved_list = interleave(operators, numbers)
    return "".join([str(x) for x in interleaved_list])


def make_a_hundred():
    one_to_nine = list(range(1, 10))

    # generate possibilities. Each possibility is the 9 numbers with
    # a set of 8 operators. Each operator can be one of three. If we
    # just generate the operators, we can interpolate them
    operators = '+- '
    operator_combos = itertools.product(operators, repeat=8)

    for operator_combo in operator_combos:
        if do_sum(one_to_nine, operator_combo) == 100:

            print("{}=100".format(create_sum_string(one_to_nine, operator_combo)))


if __name__ == "__main__":
    make_a_hundred()


# 2 Write a program that takes the duration of a year (in fractional
# days) for an imaginary planet as an input and produces a leap-year
# rule that minimizes the difference to the planet's solar year.


# 3 Implement a data structure for graphs that allows modification
# (insertion, deletion). It should be possible to store values at
# edges and nodes. It might be easiest to use a dictionary of (node,
# edgelist) to do this.


# 4 Write a function that generates a DOT representation of a graph.


# 5 Write a program that automatically generates essays for you.


# 6 Using a sample text, create a directed (multi-)graph where the
# words of a text are nodes and there is a directed edge between u
# and v if u is followed by v in your sample text. Multiple occurrences
# lead to multiple edges.


# 7 Do a random walk on this graph: Starting from an arbitrary node
# choose a random successor. If no successor exists, choose another
# random node.

morse_dict = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ' ': '       ',
}

english_dict = {}


def _reverse_dict(dict_):
    reversed_dict = {}
    for k, v in dict_.items():
        reversed_dict[v] = k

    return reversed_dict


def english_to_morse(text):
    """
    8 Write a program that automatically converts English text to Morse
    """
    return MorseMessage(text)


class MorseMessage(object):
    """
    A class to create a Morse Message
    """
    def __init__(self, english_text):
        self.letters = []
        upper_case_text = english_text.upper()
        for character in upper_case_text:
            if character not in morse_dict:
                # just ignore them for now
                # throw exception one day
                print("Ignoring {}".format(character))
                continue
            morse_dict[' '] = ' '
            self.letters.append(morse_dict[character])

    def __str__(self):
        string_ = "   ".join([str(x) for x in self.letters])
        return string_.strip()

    def to_english(self):
        global english_dict
        if english_dict == {}:
            english_dict = _reverse_dict(morse_dict)
            english_dict[' '] = ' '

        english_letters = ""
        for letter in self.letters:
            english_letters += english_dict[letter]

        return english_letters



def morse_to_english(morse_message):
    return morse_message.to_english()


# 9 Write a program that finds the longest palindromic substring of
# a given string. Try to be as efficient as possible!


# 10 Think of a good interface for a list. What operations do you
# typically need? You might want to investigate the list interface in
# your language and in some other popular languages for inspiration.


# 11 Implement your list interface using a fixed chunk of memory,
# say an array of size 100. If the user wants to add more stuff to
# your list than fits in your memory you should produce some kind of
# error, for example you can throw an exception if your language
# supports that.


# 12 Improve your previous implementation such that an arbitrary number
# of elements can be stored in your list. You can for example allocate
# bigger and bigger chunks of memory as your list grows, copy the old
# elements over and release the old storage. You should probably also
# release this memory eventually if your list shrinks enough not to need
# it anymore. Think about how much bigger the new chunk of memory should
# be so that your performance won't be killed by allocations. Increasing
# the size by 1 element for example is a bad idea.


# 13 If you chose your growth right in the previous problem, you typically
# won't allocate very often. However, adding to a big list sometimes consumes
# considerable time. That might be problematic in some applications. Instead
# try allocating new chunks of memory for new items. So when your list is full
# and the user wants to add something, allocate a new chunk of 100 elements
# instead of copying all elements over to a new large chunk. Think about where
# to do the book-keeping about which chunks you have. Different book keeping
# strategies can quite dramatically change the performance characteristics of
# your list.


# 14 Implement a binary heap. Once using a list as the base data structure and
# once by implementing a pointer-linked binary tree. Use it for implementing
# heap-sort.


# 15 Implement an unbalanced binary search tree.


# 16 Implement a balanced binary search tree of your choice. I like (a,b)-trees best.


# 17 Compare the performance of insertion, deletion and search on your
# unbalanced search tree with your balanced search tree and a sorted list.
# Think about good input sequences. If you implemented an (a,b)-tree, think
# about good values of a and b.
