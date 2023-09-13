'''
Niedokładność liczb zmiennoprzecinkowych, czyli dlaczego 0.1+0.2 != 0.3 (Floating point imprecision)

Wszystko wynika stąd, że komputer 'operuje' na języku binarnym. Oznacza to, że przy tworzeniu liczb dostępne są 
jedynie potęgi dwójki, mnożone odpowiednio przez 1 lub 0, które można sumować(tak w dużym uproszczeniu). Nic zatem 
dziwnego, że nasz float tak wygląga. No bo spróbujcie z takich liczb 
{..., 1/128, 1/64, 1/32, 1/16, 1/8, 1/4, 1/2, 0, 1, 2, 4, 8, 16, ...} 
zbudować dokładnie 0.1. Nie da się tego zazwyczaj zrobić idealnie. Teoretycznie w wyimaginowanym świecie, gdzie 
mielibyśmy nieskończoną ilość pamięci do dyspozycji i nieskończoną ilość czasu, to moglibyśmy zbliżyć się 
nieskończenie blisko, nawet ją osiągnąć czasem, do dowolnej liczby. 

Stąd ta niedokładność - wynika ona jedynie z tego jak reprezentowane są liczby zmiennoprzecinkowe w pamięci komputera. 
O ile w większości przypadków, za pomocą skończonej ilości pamięci można uzyskać zadowalającą dokładność, 
__main__tak są takie przypadki, gdzie niestety ta dokładność nie będzie wystarczająca.
'''

# asseertAlmostEqual - aby poradzic sobie z niedokładnością liczb zmiennoprzecinkowych (float), stosujemy tę metodę testową 
# domyślnie metoda porównuje do 7 miejsca po przecinku


# poniżej metoda uzyskania dokładniejszej postaci floatów
# 0.1 == 0.1000000000000000055511151231257827021181583404541015625
# 0.2 == 0.200000000000000011102230246251565404236316680908203125
# 0.2 + 0.1 == 0.3000000000000000444089209850062616169452667236328125
from decimal import Decimal

print(Decimal.from_float(0.1))      # 0.1000000000000000055511151231257827021181583404541015625  
print(Decimal.from_float(0.2))      # 0.200000000000000011102230246251565404236316680908203125
print(Decimal.from_float(0.2+0.1))  # 0.3000000000000000444089209850062616169452667236328125


import unittest

class TestClass(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(0.2 +0.1, 0.3)
    
    def test_case_2(self):
        self.assertAlmostEqual(0.2 +0.1, 0.3)
    
    def test_case_3(self):
        self.assertAlmostEqual(0.1234567, 0.1234567)
    
    def test_case_4(self):
        self.assertAlmostEqual(0.1234567, 0.1234568)        # FAIL
    
    def test_case_5(self):
        self.assertAlmostEqual(0.1234567, 0.1234568, 6)     # OK - możemy narzucić ilośc sprawdzanych miejsc po przecinku (w tym przypadku 6)
    
    def test_case_6(self):
        self.assertAlmostEqual(0.12345678, 0.12345679)      # OK - metoda zaokrągla do 7 miejsca po przecinku, dlatego wynik: OK
    
    def test_case_7(self):
        self.assertAlmostEqual(0.12345671, 0.12345679)      # FAIL


if __name__ == '__main__':
    unittest.main(verbosity=2)

'''
test_case_1 (__main__.TestClass.test_case_1) ... FAIL
test_case_2 (__main__.TestClass.test_case_2) ... ok
test_case_3 (__main__.TestClass.test_case_3) ... ok
test_case_4 (__main__.TestClass.test_case_4) ... FAIL
test_case_5 (__main__.TestClass.test_case_5) ... ok
test_case_6 (__main__.TestClass.test_case_6) ... ok
test_case_7 (__main__.TestClass.test_case_7) ... FAIL

======================================================================
FAIL: test_case_1 (__main__.TestClass.test_case_1)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/micha/pythonGit/unittest/05_assertAlmostEqual.py", line 36, in test_case_1
    self.assertEqual(0.2 +0.1, 0.3)
AssertionError: 0.30000000000000004 != 0.3

======================================================================
FAIL: test_case_4 (__main__.TestClass.test_case_4)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/micha/pythonGit/unittest/05_assertAlmostEqual.py", line 45, in test_case_4
    self.assertAlmostEqual(0.1234567, 0.1234568)        # FAIL
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 0.1234567 != 0.1234568 within 7 places (1.0000000000287557e-07 difference)

======================================================================
FAIL: test_case_7 (__main__.TestClass.test_case_7)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/micha/pythonGit/unittest/05_assertAlmostEqual.py", line 54, in test_case_7
    self.assertAlmostEqual(0.12345671, 0.12345679)      # FAIL
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 0.12345671 != 0.12345679 within 7 places (7.99999999995249e-08 difference)

----------------------------------------------------------------------
Ran 7 tests in 0.001s

FAILED (failures=3)
'''






