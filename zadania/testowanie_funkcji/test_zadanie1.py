import unittest
from zadanie1 import calc_tax

class TestCalcTax(unittest.TestCase):
    def  test_calc_tax_taxrate_023_age_18(self):
        self.assertEqual(calc_tax(1000, 0.23, 18), 230)
        self.assertEqual(calc_tax(100000, 0.23, 18), 5000)
    def  test_calc_tax_taxrate_023_age_65(self):
        self.assertEqual(calc_tax(1000, 0.23, 65), 230)
        self.assertEqual(calc_tax(100000, 0.23, 65), 23000)
    def  test_calc_tax_taxrate_023_age_66(self):
        self.assertEqual(calc_tax(1000, 0.23, 66), 230)
        self.assertEqual(calc_tax(100000, 0.23, 66), 8000)
    
    def  test_incorrect_amount_type_or_value_should_raise_error(self):
        self.assertRaises(TypeError, calc_tax, '1000', 0.23, 18)
        self.assertRaises(ValueError, calc_tax,-1000, 0.23, 65)
    def  test_incorrect_tax_rate_type_or_value_should_raise_error(self):
        self.assertRaises(TypeError, calc_tax, 1000, 1, 66)
        self.assertRaises(ValueError, calc_tax,1000, 1.23, 65)
    def  test_incorrect_age_type_or_value_should_raise_error(self):
        self.assertRaises(TypeError, calc_tax, 1000, 0.23, 18.5)
        self.assertRaises(ValueError, calc_tax,1000, 1.23, -65)
    

if __name__ == '__main__':            
    unittest.main(verbosity=2)


'''
test_calc_tax_taxrate_023_age_18 (__main__.TestCalcTax.test_calc_tax_taxrate_023_age_18) ... ok
test_calc_tax_taxrate_023_age_65 (__main__.TestCalcTax.test_calc_tax_taxrate_023_age_65) ... ok
test_calc_tax_taxrate_023_age_66 (__main__.TestCalcTax.test_calc_tax_taxrate_023_age_66) ... ok
test_incorrect_age_type_or_value_should_raise_error (__main__.TestCalcTax.test_incorrect_age_type_or_value_should_raise_error) ... ok
test_incorrect_amount_type_or_value_should_raise_error (__main__.TestCalcTax.test_incorrect_amount_type_or_value_should_raise_error) ... ok
test_incorrect_tax_rate_type_or_value_should_raise_error (__main__.TestCalcTax.test_incorrect_tax_rate_type_or_value_should_raise_error) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK
'''