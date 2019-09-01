import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_factorial(self):
         res = maths.factorial(5)
         self.assertEqual(res, 2)



if __name__ == '__main__':
    unittest.main()
        