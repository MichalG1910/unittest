import unittest


# assertGreater - arg1 większy od arg2 to OK
# assertGreaterEqual - arg1 większy równy arg2 to OK
# assertLess - arg1 mniejszy od arg2 to OK
# assertLess - arg1 mniejszy równy arg2 to OK

class TestClass(unittest.TestCase):
    def test_case_1(self):
        self.assertGreater(0.4, 0.3)

    def test_case_2(self):
        self.assertGreaterEqual(0.4, 0.4)

    def test_case_3(self):
        self.assertLess(0.4, 0.5)

    def test_case_4(self):
        self.assertLessEqual(0.5, 0.5)

    def test_case_5(self):
        self.assertGreater(0.2, 0.3)

    def test_case_6(self):
        self.assertGreaterEqual(0.3, 0.4)

    def test_case_7(self):
        self.assertLess(0.5, 0.5)

    def test_case_8(self):
        self.assertLessEqual(0.6, 0.5)


if __name__ == '__main__':
    unittest.main(verbosity=2)

'''
test_case_1 (__main__.TestClass.test_case_1) ... ok
test_case_2 (__main__.TestClass.test_case_2) ... ok
test_case_3 (__main__.TestClass.test_case_3) ... ok
test_case_4 (__main__.TestClass.test_case_4) ... ok
test_case_5 (__main__.TestClass.test_case_5) ... FAIL
test_case_6 (__main__.TestClass.test_case_6) ... FAIL
test_case_7 (__main__.TestClass.test_case_7) ... FAIL
test_case_8 (__main__.TestClass.test_case_8) ... FAIL

======================================================================
FAIL: test_case_5 (__main__.TestClass.test_case_5)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/micha/pythonGit/unittest/06_assertGreater_Equal,assertLess_Equal.py", line 18, in test_case_5
    self.assertGreater(0.2, 0.3)
AssertionError: 0.2 not greater than 0.3

======================================================================
FAIL: test_case_6 (__main__.TestClass.test_case_6)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/micha/pythonGit/unittest/06_assertGreater_Equal,assertLess_Equal.py", line 20, in test_case_6
    self.assertGreaterEqual(0.3, 0.4)
AssertionError: 0.3 not greater than or equal to 0.4

======================================================================
FAIL: test_case_7 (__main__.TestClass.test_case_7)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/micha/pythonGit/unittest/06_assertGreater_Equal,assertLess_Equal.py", line 22, in test_case_7
    self.assertLess(0.5, 0.5)
AssertionError: 0.5 not less than 0.5

======================================================================
FAIL: test_case_8 (__main__.TestClass.test_case_8)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/micha/pythonGit/unittest/06_assertGreater_Equal,assertLess_Equal.py", line 24, in test_case_8
    self.assertLessEqual(0.6, 0.5)
AssertionError: 0.6 not less than or equal to 0.5

----------------------------------------------------------------------
Ran 8 tests in 0.001s

FAILED (failures=4)
'''
