import unittest
from calculator.calc_math import SimpleMathCalculator

# aby możliwe bylo skorzystanie z pliku testowego, który znajduje sie w innym katalogu, niż testowany plik z kodem
# musimy z poziomu terminala wywołać (zwróć uwagę z poziomu jakiego katalogu wywołujesz!):
# ~/pythonGit/unittest/zadania/testowanie_klas_i_metod$ python -m unittest testCalc/test_calc.py -v


# kożystamy z test_fixtures, aby dla całego modułu stworzyć instancję klasy calc = SimpleMathCalculator(), 
# a po wykonanych testach tę instancję klasy usunąć
# można by w kazdym tescie tworzyć tą instancję indywidualnie (tak jak w zakomentowanyych fragmentach w test_cesach)
# jednak przeczyło by to zasadzie: don't repeat yourself - nie powtarzaj sam siebie
def setUpModule():
    print('setting up..')
    global calc
    calc = SimpleMathCalculator()
def tearDownModule():
    print('tearing down..')
    global calc
    del calc 

class TestSimpleMathCalculator(unittest.TestCase):
    
    def test_add(self):
        #calc = SimpleMathCalculator()
        self.assertEqual(calc.add(3,4), 7)
    def test_sub(self):
        #calc = SimpleMathCalculator()
        self.assertEqual(calc.sub(3,4), -1)
    def test_mul(self):
        #calc = SimpleMathCalculator()
        self.assertEqual(calc.mul(3,4), 12)
'''
if __name__ == '__main__':
    unittest.main(verbosity=2)
'''