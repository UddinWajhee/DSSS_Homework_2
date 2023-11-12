import unittest
from math_quiz import generate_random_integer, generate_random_operator, perform_operation


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # This Testcase help Test if random numbers generated are within the specified range mentioned
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        # This Testcase Test if the generated operator is one of the expected values
        operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random values
            rand_operator = generate_random_operator()
            self.assertIn(rand_operator, operators)

    def test_perform_operation(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 3, '*', '8 * 3', 24),
            (10, 5, '-', '10 - 5', 5),
            (4, 2, '+', '4 + 2', 6),
            (7, 2, '*', '7 * 2', 14),
            (6, 3, '*', '6 * 3', 18),
            (9, 3, '+', '9 + 3', 12),
           ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = perform_operation(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
