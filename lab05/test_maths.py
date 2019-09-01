import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        ''' Tests the add function. '''
        
        #Arrange
        result = maths.add(5,5.5)
        
        #Act - not needed
        
        #Assert
        self.assertEqual(result, 10.5, "Add function returned an incorrect result!"'')
        

    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        result = maths.fibonacci(5)
        self.assertEqual(result, 5, "Fibonacci function returned an incorrect result!")
    
    def test_convert_base_under_10(self):
        '''tests the convert_base with an under 10 base'''
        #Arrange
        result = maths.add(3,2,2)
        
        #Act - not needed 
        
        #Assert - 101 is 5 in bin
        self.assertEqual(result, "101", "Add (with base 2) function returned an incorrect result!"'')
        
    def test_convert_base_over_10(self):
        '''tests the convert_base with an over 10 base'''
        #Arrange
        result = maths.add(123124,1,16)
        
        #Act - not needed 
        
        #Assert - 1E0F5 is 123125 in hex
        self.assertEqual(result, "1E0F5", "Add (with base 16) function returned an incorrect result!"'')
        
    
    def test_convert_base_under_10_float(self):
        '''tests the covert base under 10 base but as a float number'''
        
        #Arrange
        result = maths.add(3,2.5,2)
        
        #Act - not needed 
        
        #Assert - 101 is 5 in bin
        self.assertEqual(result, "101.1", "Add (with base 2 float) function returned an incorrect result!"'')
        
    def test_convert_base_over_10_float(self):
        '''tests the covert base over 10 base but as a float number'''
        
        #Arrange
        result = maths.add(56,2.5,16)
        
        #Act - not needed 
        
        #Assert - 101 is 5 in bin
        self.assertEqual(result, "3A.8", "Add (with base 16 float) function returned an incorrect result!"'')
        
# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
