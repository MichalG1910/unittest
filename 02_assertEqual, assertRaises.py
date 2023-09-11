import unittest

# assertEqual(funkcja(arg1,arg2,...), spodziewany wynik, 'dodatkowa wiadomość gdy FAIL') porównuje wynik naszej funkcji area(4,5) z oczekiwanym wynikiem 20
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



if __name__ == '__main__':      # ten zapis powoduje uruchomienie testu bezpośrednio, ze startem skryptu (i tylko wtedy, kiedy uruchomimy plik bezpośrednio plik [nie przez np. zaimportowanie go])
    unittest.main(verbosity=2)  # verbosity=2 - pozwala wyświetlić w terminalu więcej danych związanych z przeprowadzeniem testu

# wynik test ok
'''
_assertEqual, assertRaises.py"
test_area (__main__.TestArea.test_area) ... ok
test_area_incorrect_type_should_raise_error (__main__.TestArea.test_area_incorrect_type_should_raise_error) ... ok
test_area_negative_value_should_raise_error (__main__.TestArea.test_area_negative_value_should_raise_error) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
'''
# wynik test not ok
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