# MagicMock - klasa pozwala na wywoływanie obiektów mock na metodach magicznych (implementuje większość metod magicznych)
"""
>>> from unittest.mock import Mock, MagicMock
>>> mock = Mock()
>>> magic_mock = MagicMock()
>>> mock
<Mock id='139925169208464'>
>>> magic_mock
<MagicMock id='139925189868304'>
>>> len(mock)                                                                                       # wywołanie metody len na obiekcie mock zwraca błąd
Traceback (most recent call last):
  File "/snap/pycharm-community/347/plugins/python-ce/helpers/pydev/pydevconsole.py", 
  line 364, in runcode coro = func()
                              ^^^^^^
  File "<input>", line 1, in <module>
TypeError: object of type 'Mock' has no len()
>>> len(magic_mock)                                                                                 # wywołanie metody len na obiekcie magic_mock nie zwraca błądu
0
>>> int(mock)                                                                                       # próba przekonwertowania mocka na int zwraca błęd                        
Traceback (most recent call last):
  File "/snap/pycharm-community/347/plugins/python-ce/helpers/pydev/pydevconsole.py", 
  line 364, in runcode coro = func()
                              ^^^^^^
  File "<input>", line 1, in <module>
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'Mock'
>>> int(magic_mock)                                                                                # próba przekonwertowania magic_mocka na int nie zwraca błędu
1
"""