import unittest

# assertTrue - jeśli sprawdzane wyrażenie zwraca True to test OK
# assertFalse - jeśli sprawdzane wyrażenie zwraca False to test OK

class TestClass(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(isinstance('aws', str))
    def test_case_2(self):
        self.assertTrue(isinstance('aws', int))
    def test_case_3(self):
        self.assertFalse(isinstance('aws', str))
    def test_case_4(self):
        self.assertFalse(isinstance('aws', int))
    def test_case_5(self):
        self.assertTrue(2>1)
    def test_case_6(self):
        self.assertFalse(0.1+0.2==0.3)              # 0.1 +0.2 != 0.3 - sprawdz reprezentacje liczb zmiennoprzecinkowych (05_assertAlmostEqual.py)
    
    

if __name__ == '__main__':
    unittest.main(verbosity=2)


'''
test_case_1 (__main__.TestClass.test_case_1) ... ok
test_case_2 (__main__.TestClass.test_case_2) ... FAIL
test_case_3 (__main__.TestClass.test_case_3) ... FAIL
test_case_4 (__main__.TestClass.test_case_4) ... ok
test_case_5 (__main__.TestClass.test_case_5) ... ok
test_case_6 (__main__.TestClass.test_case_6) ... ok

======================================================================
FAIL: test_case_2 (__main__.TestClass.test_case_2)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/micha/pythonGit/unittest/07_assertTrue_assertFalse.py", line 10, in test_case_2
    self.assertTrue(isinstance('aws', int))
AssertionError: False is not true

======================================================================
FAIL: test_case_3 (__main__.TestClass.test_case_3)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/micha/pythonGit/unittest/07_assertTrue_assertFalse.py", line 12, in test_case_3
    self.assertFalse(isinstance('aws', str))
AssertionError: True is not false

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (failures=2)
'''