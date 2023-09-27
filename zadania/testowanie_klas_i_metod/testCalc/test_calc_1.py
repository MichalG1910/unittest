# procedura dodawania ścieżki do katalogu, w którym python szuka modułów
#   1. Sprawdzenie, jakie katalogi są dodane do przeszukania przez python
'''
odpalamy konsole języka python poleceniem w terminalu: python
>>> import sys
>>> sys.path
['', '/usr/lib/python311.zip', '/usr/lib/python3.11', '/usr/lib/python3.11/lib-dynload', '/usr/local/lib/python3.11/dist-packages', '/usr/lib/python3/dist-packages', '/usr/lib/python3.11/dist-packages']
sys.path - jest to lista ścieżek katalogów, w których python szuka modułów (importów)
'''
#   2. Importujemy moduł systemowy, tworzymy zmienną path zawierającą naszą ścieżkę do dodania i za pomocą append dodajemy ją do sys.path
import sys
path = r'/home/micha/pythonGit/unittest/zadania/testowanie_klas_i_metod'
sys.path.append(path)
#   3. Teraz, aby odpalić plik testowy z innego katalogu niż testowany kod, wystarczy go uruchomić w standardowy sposób będąc w katalogu, w którym on się znajduje
#   ~/pythonGit/unittest/zadania/testowanie_klas_i_metod/testCalc$ python -m unittest test_calc_1.py -v    
from calculator.calc_math import SimpleMathCalculator
import unittest

# odpalamy konsole języka python
# >>> import sys
# >>> sys.path
#['', '/usr/lib/python311.zip', '/usr/lib/python3.11', '/usr/lib/python3.11/lib-dynload', '/usr/local/lib/python3.11/dist-packages', '/usr/lib/python3/dist-packages', '/usr/lib/python3.11/dist-packages']
# sys.path - jest to lista ścieżek katalogów, w których python szuka modułów (importów)


class TestSimpleMathCalculatorAdd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setting up class...') 
        cls.calc = SimpleMathCalculator()
    @classmethod
    def tearDownClass(cls):
        print('tearing down class...') 
        del cls.calc
        
    def test_add_int(self):
        self.assertEqual(self.calc.add(3,4), 7)
    def test_add_float(self):
        self.assertEqual(self.calc.add(3.0,4.0), 7.0)
    def test_add_both_negative(self):
        self.assertEqual(self.calc.add(-4,-6), -10)


class TestSimpleMathCalculatorSub(unittest.TestCase):
    def test_sub_int(self):
        calc = SimpleMathCalculator()
        self.assertEqual(calc.sub(3,4), -1)
    def test_sub_float(self):
        calc = SimpleMathCalculator()
        self.assertEqual(calc.sub(3.0,4.0), -1.0)
    def test_sub_both_negative(self):
        calc = SimpleMathCalculator()
        self.assertEqual(calc.sub(-4,-6), 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)