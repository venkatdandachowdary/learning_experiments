import unittest

from .lists_and_strings import *


class TestLargestListElement(unittest.TestCase):
    """
    """
    def test_largest_elem(self):
        items = ['1', '3444', 'chow down peoples', 'simon']
        self.assertEqual('chow down peoples', largest_element(items))


class TestReverseInPlace(unittest.TestCase):
    """
    """
    def test_reverse_in_place(self):
        items = ['1', '3444', 'chow down peoples', 'simon']
        reversed_items = list(reversed(items))
        self.assertEqual(reversed_items, reverse_in_place(items))


class TestItemInList(unittest.TestCase):
    """
    """
    def test_item_in_list(self):
        items = ['1', '3444', 'chow down peoples', 'simon']
        self.assertTrue(item_is_in_list('3444', items))
        self.assertFalse(item_is_in_list(3444, items))


class TestOddItems(unittest.TestCase):
    """
    """
    def test_odd_items(self):
        items = ['1', '3444', 'chow down peoples', 'simon', 'dave']
        self.assertEqual(['1', 'chow down peoples', 'dave',], odd_elements(items))


class TestRunningTotal(unittest.TestCase):
    """
    """
    def test_running_total(self):
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(55, running_total(items))


class TestIsPalindrome(unittest.TestCase):
    """
    """
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('aba'))
        self.assertTrue(is_palindrome('aardvarkravdraa'))
        self.assertFalse(is_palindrome('aardvarkarrdvark'))


class TestSumLoops(unittest.TestCase):
    """
    """
    def setUp(self):
        self.numbers = [1,2,3,4,5,6,7,8,9,10]
        self.numbers_2 = [10000,1000,100,10,1]

    def test_for_loop_sum(self):
        self.assertEqual(55, for_sum(self.numbers))
        self.assertEqual(11111, for_sum(self.numbers_2))

    def test_while_loop_sum(self):
        self.assertEqual(55, while_sum(self.numbers))
        self.assertEqual(11111, while_sum(self.numbers_2))

    def test_recursive_sum(self):
        self.assertEqual(55, recursive_sum(self.numbers))
        self.assertEqual(11111, recursive_sum(self.numbers_2))


class TestConcatenateLists(unittest.TestCase):
    """
    """
    def test_concat_lists(self):
        list1 = list(range(1,20))
        list2 = list(range(20,30))
        list3 = ['a', 'b', 'c']

        self.assertEqual(list(range(1, 30)), concat_lists(list1, list2))
        self.assertEqual(list(range(1, 30)) + list3, concat_lists(list1, list2, list3))


class TestAlternateLists(unittest.TestCase):
    """
    """
    def test_alternate_lists(self):
        list1 = 'abcde'
        list2 = list(range(1, 6))
        list3 = ['P', 'Q', 'R', 'S', 'T',]

        self.assertEqual(['a',1,'b',2,'c',3,'d',4,'e',5], alternate_combine(list1, list2))
        self.assertEqual(['a',1,'P','b',2,'Q','c',3,'R','d',4,'S','e',5,'T',], alternate_combine(list1, list2, list3))


class TestPigLatinify(unittest.TestCase):
    """
    """
    def test_pig_latinify(self):
        self.assertEqual(
            "Hetay uickqay rownbay oxfay",
            pig_latinify("The quick brown fox")
        )


class TestRotateList(unittest.TestCase):
    """
    """
    def test_rotate_list(self):
        self.list1 = [1,2,3,4,5,6,7,8,9,0]
        self.assertEqual(
            [3,4,5,6,7,8,9,0,1,2],
            rotate_list(self.list1, 2)
        )


class TestFibonaccio(unittest.TestCase):
    """
    """
    def test_fibonacci_func(self):
        self.fibonacci_numbers = [
            # laid out in block of ten for visual indexing
            0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
            55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181,
            6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229,
            832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986,
            102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049,
            12586269025, 20365011074, 32951280099, 53316291173, 86267571272, 139583862445, 225851433717, 365435296162, 591286729879, 956722026041,
            1548008755920, 2504730781961, 4052739537881, 6557470319842, 10610209857723, 17167680177565, 27777890035288, 44945570212853, 72723460248141, 117669030460994,
            190392490709135, 308061521170129, 498454011879264, 806515533049393, 1304969544928657, 2111485077978050, 3416454622906707, 5527939700884757, 8944394323791464, 14472334024676221,
            23416728348467685, 37889062373143906, 61305790721611591, 99194853094755497, 160500643816367088, 259695496911122585, 420196140727489673, 679891637638612258, 1100087778366101931, 1779979416004714189,
            2880067194370816120, 4660046610375530309, 7540113804746346429, 12200160415121876738, 19740274219868223167, 31940434634990099905, 51680708854858323072, 83621143489848422977, 135301852344706746049, 218922995834555169026,
        ]
        self.assertEqual(self.fibonacci_numbers, list(find_fibonacci_numbers(100)))


class TestNumberToDigits(unittest.TestCase):
    """
    """
    def test_numbers_to_digits(self):
        self.assertEqual([1,2,3,4], number_to_digits(1234))
        self.assertEqual([9,0,9,0], number_to_digits(9090))


if __name__ == '__main__':
    unittest.main()
