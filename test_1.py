import unittest
import aaa as a

class TestArea(unittest.TestCase):
    def test_area_1(self):
        self.assertEqual(a.area(4,5), 20)    
    
    def test_area_2(self):
        self.assertEqual(a.area(4,5), 21)    
    
    def test_area_3(self):
        raise AssertionError('AssertionError message')    
    
    def test_area_4(self):
        raise TypeError('OtherError message')    
    
    
if __name__ == '__main__':          # __name__ - zmienna dostępna w kazdym skrypcie i przechowująca jego nazwę  
    unittest.main(verbosity=2)