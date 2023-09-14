import unittest

# assertIn - jeśli szukany argument wystepuje w sprawdzanym kontenerze(lista, tupla, zbiór, słownik) to test OK
# assertNotIn - jeśli szukany argument NIE wystepuje w sprawdzanym kontenerze(lista, tupla, zbiór, słownik) to test OK

class TestClass(unittest.TestCase):
    def test_case_1(self):
        self.assertIn('@', 'grabarzmichal@gmail.com')
    def test_case_2(self):
        tech_stack = ['java', 'sql', 'python', 'aws']
        self.assertIn('java', tech_stack)
    def test_case_3(self):
        tech_stack = ['java', 'sql', 'python', 'aws']
        self.assertIn('c++', tech_stack)
    def test_case_4(self):
        tech_stack = {'java':'mid', 'python':'senior', 'c++':'begginer'}
        self.assertIn('c++', tech_stack)
    def test_case_5(self):
        tech_stack = {'java':'mid', 'python':'senior', 'c++':'begginer'}        # FAIL - slownik przeszukiwany jest po kluczu
        self.assertIn('mid', tech_stack)
    def test_case_6(self):
        tech_stack = {'java':'mid', 'python':'senior', 'c++':'begginer'}        
        self.assertNotIn('mid', tech_stack)
    
    
if __name__ == '__main__':
    unittest.main(verbosity=2)


'''
test_case_1 (__main__.TestClass.test_case_1) ... ok
test_case_2 (__main__.TestClass.test_case_2) ... ok
test_case_3 (__main__.TestClass.test_case_3) ... FAIL
test_case_4 (__main__.TestClass.test_case_4) ... ok
test_case_5 (__main__.TestClass.test_case_5) ... FAIL
test_case_6 (__main__.TestClass.test_case_6) ... ok

======================================================================
FAIL: test_case_3 (__main__.TestClass.test_case_3)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/micha/pythonGit/unittest/08_assertIn_assertNotIn.py", line 14, in test_case_3
    self.assertIn('c++', tech_stack)
AssertionError: 'c++' not found in ['java', 'sql', 'python', 'aws']

======================================================================
FAIL: test_case_5 (__main__.TestClass.test_case_5)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/micha/pythonGit/unittest/08_assertIn_assertNotIn.py", line 20, in test_case_5
    self.assertIn('mid', tech_stack)
AssertionError: 'mid' not found in {'java': 'mid', 'python': 'senior', 'c++': 'begginer'}

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (failures=2)
'''