import unittest
from examples import area, perimeter, calc_tax, calc_tax1
# dobrą praktyką jest wyprowadzenie testów do innego pliku poza plik z testowanym kodem. 
# aby testować taki kod korzystamy z importu

class Test_1_Area(unittest.TestCase):
    def test_area_1(self):
        self.assertEqual(area(4,5), 20)    
    
    def test_area_2(self):
        self.assertRaises(TypeError, area, '4', 5, 20)    
    
    def test_area_3(self):
        self.assertRaises(ValueError, area, 4, -5)    


class Test_2_Perimeter(unittest.TestCase):
    def test_perimeter_1(self):
        self.assertEqual(perimeter(4,5), 18)    
    
    def test_perimeter_2(self):
        self.assertRaises(TypeError, perimeter, '4', 5, 18)    
    
    def test_perimeter_3(self):
        self.assertRaises(ValueError, perimeter, 4, -5) 


class Test_3_CalcTax(unittest.TestCase):
    def test_calc_tax_with_10_percent(self):
        self.assertEqual(100, calc_tax(1000, 10))

    def test_calc_tax_with_14_percent(self):                    # Fail - 14 != 14.000000000000002 Niedokładność liczb zmiennoprzecinkowych
        self.assertEqual(14, calc_tax(100, 14)) 

    def test_calc_tax_with_14_percent_almost(self):
        self.assertAlmostEqual(14, calc_tax(100, 14)) 


class Test_4_CalcTax1(unittest.TestCase):
    def test_calc_tax1_with_10_percent(self):
        self.assertAlmostEqual(100, calc_tax1(1000, 0.1))

    def test_calc_tax1_with_14_percent(self):                    
        self.assertAlmostEqual(14, calc_tax1(100, 0.14)) 

    def test_calc_tax1_with_incorrect_amount_type_should_raise_error(self):
        self.assertRaises(TypeError, calc_tax1,'100', 0.23)
    
    def test_calc_tax1_with_incorrect_tax_rate_should_raise_error(self):
        self.assertRaises(ValueError, calc_tax1, 100, 0.0)
        self.assertRaises(ValueError, calc_tax1, 100, 1.0)
    
    def test_calc_tax1_with_incorrect_negative_amount_should_raise_error(self):
        self.assertRaises(ValueError, calc_tax1, -100, 0.23)
       
    
    
    
if __name__ == '__main__':            
    unittest.main(verbosity=2)