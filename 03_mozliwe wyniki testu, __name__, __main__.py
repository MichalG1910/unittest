# test może się zakończyć 3 wynikami: 

# OK        - test zaliczony pomyślnie
# FAIL      - test niezaliczony i podniesiony został błąd assertionError
# ERROR     - test niezaliczony i podniesiony został błąd inny niż assertionError

import unittest

# assertEqual(funkcja(arg1,arg2,...), spodziewany wynik, 'dodatkowa wiadomość gdy FAIL') porównuje wynik naszej funkcji area(4,5) z oczekiwanym wynikiem 20
# assertRaises(oczekiwany błąd, funkcja, wartośc a, wartość b) - sprawdza, czy funkcja wywoła error, gdy zostanie do niej przekazany niepoprawny argument. Jeśli funkcja wywoła oczekiwany błąd to test będzie OK, jeśli nie wywoła, to test FAIL
# assertRaises - można traktować ten test jako sprawdzenie funkcji na to, czy została w jakiś sposób zabezpieczona przez programistę przed wystąpieniem błędu


def area(width, height):
    if not (isinstance(width, (int,float)) and isinstance(height, (int,float))):
        raise TypeError('The width and height must be of type int or float.')       
    if not (width > 0 and height > 0):
        raise ValueError('The width and height must be positive.')                  
    return width * height



class TestArea(unittest.TestCase):
    def test_area_1(self):
        self.assertEqual(area(4,5), 20)    
    
    def test_area_2(self):
        self.assertEqual(area(4,5), 21)    
    
    def test_area_3(self):
        raise AssertionError('AssertionError message')    
    
    def test_area_4(self):
        raise TypeError('OtherError message')    
    
    
if __name__ == '__main__':          # __name__ - zmienna dostępna w kazdym skrypcie i przechowująca jego nazwę  
    unittest.main(verbosity=2)      # domyślnie jesli skrypt uruchamiamy bezpośrednio, to jest to __main__, jeśli jednak gdybyśmy uruchomili go w innym pliku (za pomoca import), to wtedy wyświetli nam jego nazwę 03_mozliwe wyniki testu.py 
                                    # ten zapis spowoduje, że część kodu zawarta w tej instrukcji warunkowej if zostanie uruchomiona tylko wtedy, kiedy uruchomimy skrypt bezpośrednio z pliku main. Jeśli uruchomimy go jako import, to kod w instrukcji sie nie wykona

'''
test_area_1 (__main__.TestArea.test_area_1) ... ok
test_area_2 (__main__.TestArea.test_area_2) ... FAIL
test_area_3 (__main__.TestArea.test_area_3) ... FAIL
test_area_4 (__main__.TestArea.test_area_4) ... ERROR

======================================================================
ERROR: test_area_4 (__main__.TestArea.test_area_4)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/micha/pythonGit/unittest/03_mozliwe wyniki testu.py", line 33, in test_area_4
    raise TypeError('OtherError message')
TypeError: OtherError message

======================================================================
FAIL: test_area_2 (__main__.TestArea.test_area_2)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/micha/pythonGit/unittest/03_mozliwe wyniki testu.py", line 27, in test_area_2
    self.assertEqual(area(4,5), 21)
AssertionError: 20 != 21

======================================================================
FAIL: test_area_3 (__main__.TestArea.test_area_3)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/micha/pythonGit/unittest/03_mozliwe wyniki testu.py", line 30, in test_area_3
    raise AssertionError('AssertionError message')
AssertionError: AssertionError message

----------------------------------------------------------------------
Ran 4 tests in 0.001s

FAILED (failures=2, errors=1)
'''