import unittest

from jumble_solver import solve_jumble_word


class TestJumbleSolver(unittest.TestCase):

    def setUp(self):
        self.jumble_word_1 = 'Wdnire'
        self.jumble_word_2 = 'iroz'
        self.jumble_word_3 = 'aba'
        self.jumble_word_4 = 'amtre'
        self.jumble_word_5 = 'rismch'
        self.jumble_word_6 = 'HelloWord'

    def test_jumble_word_in_dictionary(self):
        """
        Test Case for a jumble word which is present in the dictionary.txt file
        """
        result1 = solve_jumble_word(self.jumble_word_1)
        self.assertListEqual(result1["words"], ["rewind", "winder"])

        result2 = solve_jumble_word(self.jumble_word_2)
        self.assertListEqual(result2["words"], ["zori"])

        result3 = solve_jumble_word(self.jumble_word_3)
        self.assertListEqual(result3["words"], ["aba", "baa"])

        result4 = solve_jumble_word(self.jumble_word_4)
        self.assertListEqual(result4["words"], ["armet", "mater", "ramet", "tamer"])

        result5 = solve_jumble_word(self.jumble_word_5)
        self.assertListEqual(result5["words"], ["chirms", "chrism", "smirch"])

    def test_jumble_word_not_in_dictionary(self):
        """
        Test Case for a jumble word which is not present in the dictionary.txt file
        """
        result = solve_jumble_word(self.jumble_word_6)
        self.assertEqual(result["message"], "Sorry! No word is present for %s" % self.jumble_word_6)


if __name__ == '__main__':
    unittest.main()
