import unittest

# assertRaises(oczekiwany błąd, funkcja, wartośc a, wartość b) - sprawdza, czy funkcja wywoła error, gdy zostanie do niej przekazany niepoprawny argument. Jeśli funkcja wywoła oczekiwany błąd to test będzie OK, jeśli nie wywoła, to test FAIL
# assertRaises - można traktować ten test jako sprawdzenie funkcji na to, czy została w jakiś sposób zabezpieczona przez programistę przed wystąpieniem błędu
# oczekiwany błąd staramy się podać dokładnie (np. IndexError). Kiedy nie wiemy, jaki błąd zostanie wywołany, korzystamy z Exception, która odpowiada za wszystkie błędy

def get_value(index,container):
    return container[index]

print(get_value(2,'python'))            # t
print(get_value(2,[1,2,3,4,5,6]))       # 3



class TestClass(unittest.TestCase):
    def test_case_1(self):
        self.assertRaises(IndexError, get_value,6, 'python')
    
    def test_case_2(self):
        self.assertRaises(Exception, get_value,6, 'python')     # Exception - odpowiada za wszystkie błędy
    
    def test_case_3(self):
        with self.assertRaises(IndexError):                     # test przy użyciu context managera - ten test jest rownoznaczny z test_case_1
            get_value(6,'python')
    
    def test_case_4(self):
        with self.assertRaises(IndexError):
            get_value(2,'aws')
    
    
if __name__ == '__main__':
    unittest.main(verbosity=2)


'''
test_case_1 (__main__.TestClass.test_case_1) ... ok
test_case_2 (__main__.TestClass.test_case_2) ... ok
test_case_3 (__main__.TestClass.test_case_3) ... ok
test_case_4 (__main__.TestClass.test_case_4) ... FAIL

======================================================================
FAIL: test_case_4 (__main__.TestClass.test_case_4)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/micha/pythonGit/unittest/10_assertRaises.py", line 27, in test_case_4
    with self.assertRaises(IndexError):
AssertionError: IndexError not raised

----------------------------------------------------------------------
Ran 4 tests in 0.000s

FAILED (failures=1)
'''