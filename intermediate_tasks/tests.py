import unittest

from .intermediate_tasks import *


class TestMorseFunctions(unittest.TestCase):
    """
    """
    def setUp(self):
        self.english = "The quick brown fox jumped over the lazy cow"
        self.morse = "-   ....   .       --.-   ..-   ..   -.-.   -.-" + \
                     "       -...   .-.   ---   .--   -.       ..-.   -" + \
                     "--   -..-       .---   ..-   --   .--.   .   -..   " + \
                     "    ---   ...-   .   .-.       -   ....   .       .-." + \
                     ".   .-   --..   -.--       -.-.   ---   .--"

    def test_english_to_morse(self):
        morse = english_to_morse(self.english)
        print(str(morse))
        self.assertEqual(self.morse, str(morse))

    def test_morse_to_english(self):
        morse = english_to_morse(self.english)
        english = str(morse_to_english(morse))
        self.assertEqual(self.english.upper(), english)


if __name__ == '__main__':
    unittest.main()
