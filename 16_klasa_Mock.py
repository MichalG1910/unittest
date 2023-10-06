# Mock to obiekt, którego używa się zamiast rzeczywistej implementacji w trakcie testów jednostkowych. Pozwala on na określenie 
# jakich interakcji spodziewamy się w trakcie testów. Następnie można sprawdzić czy spodziewane interakcje rzeczywiście wystąpiły.

'''
Mockowanie, czyli naśladowanie czegoś, jakiegoś zachowania. W polskim tłumaczeniu można się spotkać z różnymi tłumaczeniami słowa mock, 
między innymi makieta. Jeżeli metoda, ma w sobie logikę oraz korzysta z zewnętrznych zasobów (takich jak bazadanych, plik, webserwisy itp.), 
to w naszych testach jednostkowych nie dałoby się takiej metody testować. Jeżeli natomiast podstawimy w miejsce zewnętrznego zasobu, 
jakiś sztuczny obiekt, który nie ma żadnej logiki, to wtedy jak najbardziej uda nam się taką metodę testować. Żeby taki zabieg nam się 
udał, nasz kod musi stosować się do pewnych zasad. Między innymi musi mieć luźne powiązania i operować na interfejsach. Jeżeli stosujemy 
się do tych zasad, to dzięki temu możemy podmienić implementacje na potrzeby testów. Dlatego, jeżeli chcemy dodać testy do jakichś 
aplikacji, które nie były pisane z myślą o testach, to tutaj może pojawić się problem. Musimy taki kod zrefaktoryzować, co bez 
wcześniejszych testów może być dużym wyzwaniem.
'''

# uruchamiamy konsolę python, aby potestować klasę mock
'''
micha@micha-GF63-Thin-10UC:~$ python
Python 3.11.4 (main, Jun  9 2023, 07:59:55) [GCC 12.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> from unittest.mock import Mock                          # importujemy klase Mock
>>> mock = Mock()                                           # tworzymy instancję(obiekt) klasy mock
>>> mock                                                    # wyświetlamy nasz obiekt do konsoli
<Mock id='139813369721808'>                                 # otrzymujemy w wyniku ID mocka  
>>> mock.first_name                                         # kiedy wywołamy mock z dodatkowym atrybutem, który nie istnieje, 
<Mock name='mock.first_name' id='139813354407248'>          # to zostanie utworzony nowy obiekt mock z nowym ID 
>>> mock.first_name                                         # kiedy wywołamy istniejący mock jeszcze raz, 
<Mock name='mock.first_name' id='139813354407248'>          # to otrzymamy ten sam ID   
>>> mock()                                                  # wywołanie naszego mocka jak funkcji(), 
<Mock name='mock()' id='139813345278416'>                   # spowoduje powstanie nowego mocka z nowym ID        

>>> mock = Mock(name='first_mock')                          # tworzenie mocka z atrybutem nazwy name
>>> mock                                                    # wyświetlamy go w konsoli,
<Mock name='first_mock' id='139813354410512'>               # opis tak stworzonego mocka z name
>>> mock.first_name                                         # jeśli utworzymy kolejnego mocka z nie istniejącym atrybutem w ten sposób,
<Mock name='first_mock.first_name' id='139813345279312'>    # to otrzymamy nowy mock z taką nazwą

>>> mock = Mock(return_value='John')                        # tworzenie mocka z atrybutem zwracanej wartości return_value
>>> mock()                                                  # po wywołaniu go, zamiast otrzymac nowy mock,
'John'                                                      # zwróci nam naszą zdefiniowaną wartość 

>>> mock = Mock()                                           # tworzenie mocka z atrybutem return_value w inny sposób
>>> mock
<Mock id='139813345279504'>
>>> mock.return_value = 'Smith'
>>> mock()
'Smith'
>>> mock.return_value = 10
>>> mock()
10

                                                            # tworzenie mocka z atrybutem side_effect (pozwala ustawiać 3 różne wartości obiektów: wywoływalne, iterowalne, wyjątki)
mock = Mock(side_effect = IndexError('Error message.'))     # mock podnoszący błąd IndexError z naszym message 
>>> mock                                                    
<Mock id='140075995292432'> 
>>> mock()                                                  # wywołujemy nasz mock. Poniżej cały błąd, który wyświetliło

Traceback (most recent call last):
  File "/snap/pycharm-community/347/plugins/python-ce/helpers/pydev/pydevconsole.py", line 364, in runcode
    coro = func()
           ^^^^^^
  File "<input>", line 1, in <module>
  File "/usr/lib/python3.11/unittest/mock.py", line 1124, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1128, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/unittest/mock.py", line 1183, in _execute_mock_call
    raise effect
IndexError: Error message. 


>>> mock = Mock()                                                   # wywołujemy mocka z różnymi argumentami
>>> mock()
<Mock name='mock()' id='140075955752016'>
>>> mock(3,4)
<Mock name='mock()' id='140075955752016'>
>>> mock(0,5)
<Mock name='mock()' id='140075955752016'>
>>> mock(22,45)
<Mock name='mock()' id='140075955752016'>

# poniżej drzewo przechowywanych danych nt. nazego mocka (wyświetlane w konsoli python w pycharm)
mock = {Mock} <Mock id='140075955758608'>
 call_args = {_Call: 2} call(22, 45)
 call_args_list = {_CallList: 4} [call(), call(3, 4), call(0, 5), call(22, 45)]
 call_count = {int} 4
 called = {bool} True
 im_self = {Mock} <Mock name='mock.im_self' id='140075955763024'>
 method_calls = {_CallList: 0} []
 mock_calls = {_CallList: 4} [call(), call(3, 4), call(0, 5), call(22, 45)]
 return_value = {Mock} <Mock name='mock()' id='140075955752016'>
 shape = {Mock} <Mock name='mock.shape' id='140075955760592'>
 side_effect = {NoneType} None


 # poniżej przykład mockowania funkcji random, zwracającej losowy element listy [4,5,6,7]. Trudno byłoby przeprowadzić test na takiej 
 # funkcji, ponieważ zwracany wynik jest losowy. Aby temu zapobiec, zmockujemy funkcje random, i przypiszemy jej jeden konkretny wynik, 
 # jaki zwróci za każdym razem, kiedy ją wywołamy


 >>> import random
>>> random.choice([4,5,6,7])                                        # wywołanie random.choice zwraca losowy element naszej przekazanej listy
4
>>> random.choice([4,5,6,7])
6
>>> random.choice([4,5,6,7])
6
>>> random.choice([4,5,6,7])
4
>>> random.choice = Mock(return_value=6)                            # po zmockowaniu retur_value=6, za kazdym razem mock zwraca wartość 6
>>> random.choice()
6
>>> random.choice()
6
>>> random.choice()
6
>>> random.choice()
6


>>> random.choice = Mock()                                          # tworzymy mocka
>>> mock
<Mock id='140075955758608'>
>>> random.choice.assert_called()                                   # wywołujemy na nim metode assert_called(), która oczekuje, że mock był wywołany. Nasz nie był - zwróciło błąd
Traceback (most recent call last):
  File "/snap/pycharm-community/347/plugins/python-ce/helpers/pydev/pydevconsole.py", line 364, in runcode
    coro = func()
           ^^^^^^
  File "<input>", line 1, in <module>
  File "/usr/lib/python3.11/unittest/mock.py", line 908, in assert_called
    raise AssertionError(msg)
AssertionError: Expected 'mock' to have been called.

random.choice()                                                     # po wywołaniu naszego mocka, assert_called nie zwraca już błędu
<Mock name='mock()' id='140075955853264'>
random.choice.assert_called()
'''

aaaaaaaaaaaaaaaaaaaaaa