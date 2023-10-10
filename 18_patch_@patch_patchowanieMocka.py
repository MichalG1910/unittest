import random
import unittest
from unittest.mock import Mock, patch

# mockowanie  funkcji random.radint przy uzyciu patch

print('# normalne działanie funkcji') 
for i in range(5):
    print(random.randint(1,6), end=' ')
    
print()
print('# mockujemy działanie funkcji random.randint przy użuciu patch (context manager)')
with patch('random.randint') as mock_random:
    mock_random.return_value = 5
    for i in range(5):
        print(random.randint(1,6), end=' ')

print()
print('# mock działa tylko w tym kawalku kodu, napisanym w context_manager. Jeśli znowu uzyjemy random.randint, zwróci nam losowe liczby')
for i in range(5):
    print(random.randint(1,6), end=' ')

print()
print('# tworzenie mocka bez context_managera i patch.')
random.randint = Mock(return_value=1)
for i in range(5):
    print(random.randint(1, 6), end=' ')

print()
print('# skorzystanie dalej z random.randint, dalej zwraca naszego mocka = 1')
for i in range(5):
    print(random.randint(1, 6), end=' ')
print()

# dekorator @patch
print('mockowanie przy pomocy dekoratora @patch')
def get_value():
    return random.randint(1,9)
def get_value_cx():
        rand_int = random.randint(1,9)
        return f'CX-{rand_int}'

@patch('random.randint')                                    # uzywamy dekoratora @patch na random.randint
def test_get_value(mock_random):
    mock_random.return_value = 3                            # tworzymy obiekt mock i przypisujemy mu zwracana wartość = 3
    result = get_value()                                    # zmienna przechowa wynik funkcji get_value()
    assert result == 3                                      # wykonujemy aserację na tej zmiennej 
    assert mock_random.call_count == 1                      # wykonujemy aserację - sprawdzamy ilość wywołań mocka  
test_get_value()                                            # uruchamiamy nasza funkcję aserującą test_get_value()

print('\nTest - mockowanie przy pomocy dekoratora @patch')
class TestGetValue(unittest.TestCase):
    
    @patch('random.randint')
    def test_get_value(self, mock_random):
        mock_random.return_value = 3
        self.assertEqual(get_value(), 3)
    
    @patch('random.randint')
    def test_get_value_cx(self, mock_random):
        mock_random.return_value = 3
        actual = get_value_cx()
        expected = 'CX-3'
        self.assertEqual(actual, expected)
        
    @patch('random.randint')
    def test_get_value_call_count(self, mock_random):
        get_value()
        self.assertEqual(mock_random.call_count, 1)


unittest.main(verbosity=2)                                  # uwaga, dla pycharm musisz zakomentowac te linię

    