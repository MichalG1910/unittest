import unittest

# Kolejne przykłady testów tym razem sprawdzające metody wbudowane w język python (.split(), .join(), .islower())

# assertTrue - sprawdza, czy fragment kodu zwraca wartość TRUE. Jeśli tak, test jest OK, jeśli nie FAIL

class TestClass(unittest.TestCase):
    
    def test_case_1(self):
        self.assertEqual('John Smith'.split(), ['John', 'Smith'])
    
    def test_case_2(self):
        self.assertEqual('3.9'.split('.'), ['3', '9'])
    
    def test_case_3(self):
        self.assertEqual('#'.join(['sport', 'gym']), 'sport#gym')
    
    def test_case_4(self):
        self.assertTrue('apple'.islower()) 

# UWAGA!!! Testy są niezależne od siebie, kolejność wykonywania testów jest zgodna z alfabetem według nazwy testu, a nie kolejności wystąpienia
# To samo tyczy się klas testowych. Również zostaną one wykonane zgodnie z alfabetem według nazwy klasy 


# python -m unittest 04_assertTrue_kolejne_przyklady_testow.py -v            