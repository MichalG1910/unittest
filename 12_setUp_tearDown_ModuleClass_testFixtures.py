import unittest

### Test Fixtures - przygotowanie środowiska do testów ###
# Nie można zmienić nazwy funkcji Test Fixtures
# def setUpModule() - pozwala wykonać blok kodu na poczatku całego modułu testowego (przydatne, aby np. połączyć sie z DB)
# def tearDownModule() - pozwala wykonać blok kodu na końcu całego modułu testowego (przydatne, aby np. odłączyć się od DB)
# @classmethod def setUpClass(cls) - pozwala wykonać blok kodu na początku klasy testowej (korzystamy z dekoratora @classmethod) 
# @classmethod def tearDownClass(cls) - pozwala wykonać blok kodu na końcu klasy testowej (korzystamy z dekoratora @classmethod)
# def setUp(self) - pozwala wykonać blok kodu na początku każdego test_case w danej klasie testowej 
# def tearDown(self) - pozwala wykonać blok kodu na końcu każdego test_case w danej klasie testowej 


# definiujemy nasze funkcje z blokiem kodu (poczatek i koniec całego modułu)
def setUpModule():
    print('setting up module...')
def tearDownModule():
    print('tearing down module...')

class TestClass1(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual('John Smith'.split(), ['John', 'Smith'])

class TestClass2(unittest.TestCase):

    # definiujemy nasze funkcje z blokiem kodu (początek i koniec klasy)
    @classmethod
    def setUpClass(cls) :
        print(f'seting up class... {cls.__name__}')     # {cls.__name__} - aby w naszym kodzie wydrukowało nazœ klasy
    @classmethod
    def tearDownClass(cls) :
        print(f'tearig down class... {cls.__name__}')
    
    # definiujemy nasze funkcje z blokiem kodu (początek i koniec każdego test_case w klasie)
    def setUp(self):
        print('setting up...')
    def tearDown(self):
        print('tearing down...')
    
    def test_case_1(self):
        self.assertEqual('3.9'.split('.'), ['3', '9'])
    def test_case_2(self):
        self.assertEqual('3.9'.split('.'), ['3', '9'])

class TestClass3(unittest.TestCase):   
    def test_case_1(self):
        self.assertEqual('#'.join(['sport', 'gym']), 'sport#gym')


if __name__ == '__main__':
    unittest.main(verbosity=2)