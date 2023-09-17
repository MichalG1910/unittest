import unittest
from datetime import date
import sys

# @unittest.skip('Komunikat pomijania testu') - dekorator słuzy do pomijania testu. Test zostanie pominiety za każdym razem
# @unittest.skipIf(warunek, 'komunikat jesli pomija test') - pomija test, jesli warunek jest True
# @unittest.skipUnless(warunek, 'komunikat jesli pomija test') - dekorator pomija test, chyba że spełniony jest warunek (True)

print(date.today().day)                     # dzisiejszy  numer dnia w miesiącu
print(date.today().day % 2)                 # korzystamy z modulo, aby sprawdzić, czy jest on parzysty, czy nie (jeśli wynik=1 - nieparzysty, wynik=0 - parzysty)
print(sys.platform)                         # sprawdzamy system operacyjny
print(sys.platform.startswith('linux'))     # True (dla linux)

class TestClass(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual('aws'.upper(), 'AWS')
    @unittest.skip('Komunikat pomijania testu...')
    def test_case_2(self):
        self.assertEqual('aws'.upper(), 'AWS')
    
    # @unittest.skipIf() - jako warunek używamy wyrażenia logicznego, aby sprawdzić, czy dzien jest parzysty, czy nie (wykonywano 17 wrzesnia)
    # date.today().day % 2 != 0 - True, pominie nam dni nieparzyste (dla 17 września)
    # date.today().day % 2 == 0 - False, pominie nam dni parzyste (dla 17 września)
    @unittest.skipIf(date.today().day % 2 != 0, 'skipping odd days...')
    def test_case_3(self):
        self.assertEqual('aws'.upper(), 'AWS')
    @unittest.skipIf(date.today().day % 2 == 0, 'skipping even days...')
    def test_case_4(self):
        self.assertEqual('aws'.upper(), 'AWS')
    
    # @unittest.skipUnless() - jako warunek przyjmujemy testowanie na odpowiednim systemie operacyjnym (wykonywano na linux)
    # sys.platform.startswith('linux') - True, warunek spełniony (platforma linux), test zostanie uruchomiony
    # sys.platform.startswith('win') - False, warunek nie spełniony (platforma linux), test zostanie pominięty
    @unittest.skipUnless(sys.platform.startswith('linux'), 'Requires Linux...')
    def test_case_5(self):
        self.assertEqual('aws'.upper(), 'AWS')
    @unittest.skipUnless(sys.platform.startswith('win'), 'Requires Windows...')
    def test_case_6(self):
        self.assertEqual('aws'.upper(), 'AWS')

if __name__ == '__main__':
    unittest.main(verbosity=2)


'''
test_case_1 (__main__.TestClass.test_case_1) ... ok
test_case_2 (__main__.TestClass.test_case_2) ... skipped 'Komunikat pomijania testu...'
test_case_3 (__main__.TestClass.test_case_3) ... skipped 'skipping odd days...'
test_case_4 (__main__.TestClass.test_case_4) ... ok
test_case_5 (__main__.TestClass.test_case_5) ... ok
test_case_6 (__main__.TestClass.test_case_6) ... skipped 'Requires Windows...'

----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK (skipped=3)
'''