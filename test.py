import unittest
import guessing_game


class TestGame(unittest.TestCase):
    def test_wrong_answer(self):
        result = guessing_game.guessing(2, 3, 1, 20)
        self.assertEqual(result, 'Try again :(')  # add assertion here

    def test_out_of_range(self):
        result = guessing_game.guessing(2, 11, 1, 10)
        self.assertEqual(result, 'Give a number 1~10.')

    def test_text_instead_of_number(self):
        result = guessing_game.guessing(2, 'sdf', 1, 10)
        self.assertEqual(result, 'Give a number 1~10.')

    def test_right_answer(self):
        result = guessing_game.guessing(2, 2, 1, 10)
        self.assertEqual(result, 'You won :)')

    def test_answer_none(self):
        result = guessing_game.guessing(2, None, 1, 10)
        self.assertEqual(result, 'Give a number 1~10.')


if __name__ == '__main__':
    unittest.main()
