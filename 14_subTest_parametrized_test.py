import unittest
from parameterized import parameterized         # specjalny moduł do parametryzacji testów (użyty w klasie 3 - class TestWithParametrizedDecorator(unittest.TestCase):)


# Parametrized test - kiedy mamy do wykonania wiele podobnych testów, zamiast robić to w wielu test_case,
# można przy pomocy pętli for wykonać to w jednym test_case. 
# róznica jest taka, że wykonanie wielu przypadków testowych w 1 test_case bez pętli for w przypadku Fail, zawsze zwróci tylko pierwszy z blędów (nie wykona kolejnych przypadków),
# natomiast przy użyciu pętli for wykona wszystkie przypadki i zwróci wszystkie Fail, jakie znajdzie

class SimpleMathCalculator:
    def add(self, x, y):
        return x + y
    def sub(self, x, y):
        return x - y
    def mul(self, x, y):
        return x * y
    def true_div(self, x, y):
        return x / y
    def floor_div(self, x, y):
        return x // y
    

class TestSimpleMathCalculatorWithoutForLoop(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleMathCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(-3, -2), -5)
        self.assertEqual(self.calc.add(-3, 2), -1)
        self.assertEqual(self.calc.add(3, -2), 1)
        self.assertEqual(self.calc.add(3, 2), 5)


class TestSimpleMathCalculatorWithForLoop(unittest.TestCase): 
    def setUp(self):
        self.calc = SimpleMathCalculator()

    def test_add1(self):
        cases = [(-3,-2,-5), (-3,2,-1), (3,-2,-1), (3,2,-5)]

        for x, y, result in cases:
            with self.subTest(cases=cases):                     # aby każdy przypadek był rozpatrywany oddzielnie używamy context managera
                self.assertEqual(self.calc.add(x, y), result)

# w klasie poniżej do parametryzacji testów używamy specjalnego modułu parametrized
class TestWithParametrizedDecorator(unittest.TestCase): 
    def setUp(self):
        self.calc = SimpleMathCalculator()
    
    # stosujemy specjalny dekorator, za pomocą metody expand dodajemy listę tupli z kolejnymi przypadkami, które zostaną załadowane do test_case
    # oprócz niezbędnych parametrów, możemy przekazać w pierwszym indeksie tupli nazwę, jaką chcemy zobaczyć w opisie każdego przypadku
    @parameterized.expand([('negative',-3,-2,-5), ('mixed',-3,2,1), ('positive',3,2,5)])

    def test_add(self, name, x, y, result):     # w test_case oprócz self, przekazujemy parametry, zgodnie z tym, co przekazaliśmy w dekoratorze
        self.assertEqual(self.calc.add(x, y), result)

if __name__ == '__main__':
    unittest.main(verbosity=2)


'''
test_add1 (__main__.TestSimpleMathCalculatorWithForLoop.test_add1) ... 
  test_add1 (__main__.TestSimpleMathCalculatorWithForLoop.test_add1) (cases=[(-3, -2, -5), (-3, 2, -1), (3, -2, -1), (3, 2, -5)]) ... FAIL
  test_add1 (__main__.TestSimpleMathCalculatorWithForLoop.test_add1) (cases=[(-3, -2, -5), (-3, 2, -1), (3, -2, -1), (3, 2, -5)]) ... FAIL
test_add (__main__.TestSimpleMathCalculatorWithoutForLoop.test_add) ... ok
test_add_0_negative (__main__.TestWithParametrizedDecorator.test_add_0_negative) ... ok
test_add_1_mixed (__main__.TestWithParametrizedDecorator.test_add_1_mixed) ... FAIL
test_add_2_positive (__main__.TestWithParametrizedDecorator.test_add_2_positive) ... ok

======================================================================
FAIL: test_add1 (__main__.TestSimpleMathCalculatorWithForLoop.test_add1) (cases=[(-3, -2, -5), (-3, 2, -1), (3, -2, -1), (3, 2, -5)])
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/micha/pythonGit/unittest/14_subTest_parametrized_test.py", line 43, in test_add1
    self.assertEqual(self.calc.add(x, y), result)
AssertionError: 1 != -1

======================================================================
FAIL: test_add1 (__main__.TestSimpleMathCalculatorWithForLoop.test_add1) (cases=[(-3, -2, -5), (-3, 2, -1), (3, -2, -1), (3, 2, -5)])
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/micha/pythonGit/unittest/14_subTest_parametrized_test.py", line 43, in test_add1
    self.assertEqual(self.calc.add(x, y), result)
AssertionError: 5 != -5

======================================================================
FAIL: test_add_1_mixed (__main__.TestWithParametrizedDecorator.test_add_1_mixed)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/parameterized/parameterized.py", line 637, in standalone_func
    return func(*(a + p.args), **p.kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/micha/pythonGit/unittest/14_subTest_parametrized_test.py", line 52, in test_add
    self.assertEqual(self.calc.add(x, y), result)
AssertionError: -1 != 1

----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (failures=3)
'''