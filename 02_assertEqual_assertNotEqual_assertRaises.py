# dokumentacja unittest: https://docs.python.org/3/library/unittest.html


import unittest

# assertEqual(funkcja(arg1,arg2,...), spodziewany wynik, 'dodatkowa wiadomość gdy FAIL') porównuje wynik naszej funkcji area(4,5) z oczekiwanym wynikiem 20
# assertNotEqual - metoda daje OK kiedy oczekiwany wynik jest inny niż argument/wynik funkcji sprawdzanej. Działa odwrotnie do assertEqual
# assertRaises(oczekiwany błąd, funkcja, wartośc a, wartość b) - sprawdza, czy funkcja wywoła error, gdy zostanie do niej przekazany niepoprawny argument. Jeśli funkcja wywoła oczekiwany błąd to test będzie OK, jeśli nie wywoła, to test FAIL
# assertRaises - można traktować ten test jako sprawdzenie funkcji na to, czy została w jakiś sposób zabezpieczona przez programistę przed wystąpieniem błędu


# funkcja sprawdza czy wysokośc i szerokośc są int lub float i czy sa większe od 0
def area(width, height):
    if not (isinstance(width, (int,float)) and isinstance(height, (int,float))):
        raise TypeError('The width and height must be of type int or float.')       # jeśli width, height nie będzie typem int lub float asercja zwróci TypeError
    if not (width > 0 and height > 0):
        raise ValueError('The width and height must be positive.')                  # jeśli width, height nie będzie > 0 asercja zwróci ValueError
    return width * height
    
assert(area(4,5)==20)


# tworzymy klase testową dziedziczącą z klasy unittest.TestCase 
class TestArea(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(4,5), 20, 'dodatkowa wiadomość gdy FAIL')    # assertEquals - porównuje wynik naszej funkcji area(4,5) z oczekiwanym wynikiem 20
    
    def test_area_incorrect_type_should_raise_error(self):
        self.assertRaises(TypeError, area,'4',5)                           # assertRaises(oczekiwany błąd, funkcja, wartośc a, wartość b) - sprawdza, czy funkcja wywoła error, gdy zostanie do niej przekazany niepoprawny argument. Jeśli funkcja wywoła oczekiwany błąd to test będzie OK, jeśli nie wywoła, to test FAIL
        self.assertRaises(TypeError, area,4,'5')                           # w tym przypadku szukamy błędu typu TypeError, 1 przekazany argument jest błędny (string zamiast liczby)
                                                                           # jednak w tym przypadku w funkcji zastosowaliśmy instrukcję warunkowa, która wywoła nam ten błąd (TypeError), więc test będzie OK
    def test_area_negative_value_should_raise_error(self):
        self.assertRaises(ValueError, area,-4,5)                           # w tym przypadku sprawdzamy ValueError - -4 jest błędne
        self.assertRaises(ValueError, area,4,-5)


# wynik test ok (3 pierwsze testy)
'''
_assertEqual, assertRaises.py"
test_area (__main__.TestArea.test_area) ... ok
test_area_incorrect_type_should_raise_error (__main__.TestArea.test_area_incorrect_type_should_raise_error) ... ok
test_area_negative_value_should_raise_error (__main__.TestArea.test_area_negative_value_should_raise_error) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
'''
# wynik test not ok (3 pierwsze testy)
'''
_assertEqual, assertRaises.py"
test_area (__main__.TestArea.test_area) ... ok
test_area_incorrect_type_should_raise_error (__main__.TestArea.test_area_incorrect_type_should_raise_error) ... ok
test_area_negative_value_should_raise_error (__main__.TestArea.test_area_negative_value_should_raise_error) ... FAIL

======================================================================
FAIL: test_area_negative_value_should_raise_error (__main__.TestArea.test_area_negative_value_should_raise_error)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/micha/pythonGit/unittest/02_assertEqual, assertRaises.py", line 24, in test_area_negative_value_should_raise_error
    self.assertRaises(ValueError, area,-4,5)
AssertionError: ValueError not raised by area

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)
'''

class TestClass(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual('aws'.upper(), 'AWS')   
    
    def test_case_2(self):
        self.assertEqual('aws'.upper(), 'aws')   
    
    def test_case_3(self):
        self.assertEqual('3.5.9'.split('.'), ['3','5','9'])   
    
    def test_case_4(self):
        self.assertEqual('3.5.9'.split('.'), ['3','5',9])   
    
    def test_case_5(self):
        self.assertEqual({3,4,5}, {5,3,4})   
    
    def test_case_6(self):
        self.assertEqual({3,4,5}, {5,3,4,6})

    def test_case_7(self):
        self.assertNotEqual('aws'.upper(), 'AWS')   
    
    def test_case_8(self):
        self.assertNotEqual('aws'.upper(), 'aws')   
    
    
if __name__ == '__main__':      # ten zapis powoduje uruchomienie testu bezpośrednio, ze startem skryptu (i tylko wtedy, kiedy uruchomimy plik bezpośrednio plik [nie przez np. zaimportowanie go])
    unittest.main(verbosity=2)  # verbosity=2 - pozwala wyświetlić w terminalu więcej danych związanych z przeprowadzeniem testu


# metoda testowa assertEqual daje nam możliwość testowania wielu typów danych np. list, tupli, zbiorów.
# zwróć uwagę, że dostajemy różne podsumowania testów FAIL w zalezności jakie dane testujemy.
'''
test_area (__main__.TestArea.test_area) ... ok
test_area_incorrect_type_should_raise_error (__main__.TestArea.test_area_incorrect_type_should_raise_error) ... ok
test_area_negative_value_should_raise_error (__main__.TestArea.test_area_negative_value_should_raise_error) ... ok
test_case_1 (__main__.TestClass.test_case_1) ... ok
test_case_2 (__main__.TestClass.test_case_2) ... FAIL
test_case_3 (__main__.TestClass.test_case_3) ... ok
test_case_4 (__main__.TestClass.test_case_4) ... FAIL
test_case_5 (__main__.TestClass.test_case_5) ... ok
test_case_6 (__main__.TestClass.test_case_6) ... FAIL
test_case_7 (__main__.TestClass.test_case_7) ... FAIL
test_case_8 (__main__.TestClass.test_case_8) ... ok

======================================================================
FAIL: test_case_2 (__main__.TestClass.test_case_2)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/micha/pythonGit/unittest/02_assertEqual, assertRaises.py", line 70, in test_case_2
    self.assertEqual('aws'.upper(), 'aws')
AssertionError: 'AWS' != 'aws'
- AWS
+ aws


======================================================================
FAIL: test_case_4 (__main__.TestClass.test_case_4)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/micha/pythonGit/unittest/02_assertEqual, assertRaises.py", line 76, in test_case_4
    self.assertEqual('3.5.9'.split('.'), ['3','5',9])
AssertionError: Lists differ: ['3', '5', '9'] != ['3', '5', 9]

First differing element 2:
'9'
9

- ['3', '5', '9']
?            - -

+ ['3', '5', 9]

======================================================================
FAIL: test_case_6 (__main__.TestClass.test_case_6)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/micha/pythonGit/unittest/02_assertEqual, assertRaises.py", line 82, in test_case_6
    self.assertEqual({3,4,5}, {5,3,4,6})
AssertionError: Items in the second set but not the first:
6

======================================================================
FAIL: test_case_7 (__main__.TestClass.test_case_7)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/micha/pythonGit/unittest/02_assertEqual, assertRaises.py", line 85, in test_case_7
    self.assertNotEqual('aws'.upper(), 'AWS')
AssertionError: 'AWS' == 'AWS'

----------------------------------------------------------------------
Ran 11 tests in 0.001s

FAILED (failures=4)
'''