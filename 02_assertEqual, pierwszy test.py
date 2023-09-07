import unittest

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
        self.assertEqual(area(4,6), 20, 'dodatkowa wiadomość gdy FAIL')    # assertEquals - porównuje wynik naszej funkcji area(4,5) z oczekiwanym wynikiem 20

if __name__ == '__main__':      # ten zapis powoduje uruchomienie testu bezpośrednio, ze startem skryptu
    unittest.main(verbosity=2)  # verbosity=2 - pozwala wyświetlić w terminalu więcej danych związanych z przeprowadzeniem testu

# wynik test ok
'''
test_area (__main__.TestArea.test_area) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
'''
# wynik test not ok
'''
test_area (__main__.TestArea.test_area) ... FAIL

======================================================================
FAIL: test_area (__main__.TestArea.test_area)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/micha/pythonGit/unittest/02_assertEqual, pierwszy test.py", line 17, in test_area
    self.assertEqual(area(4,6), 20, 'dodatkowa wiadomość gdy FAIL')    # assertEquals - porównuje wynik naszej funkcji area(4,5) z oczekiwanym wynikiem 20
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 24 != 20 : dodatkowa wiadomość gdy FAIL

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
'''