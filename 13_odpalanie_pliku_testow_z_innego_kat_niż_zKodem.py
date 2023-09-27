# aby odpalić plik testów z innego katalogu niż ten z kodem:

### metoda 1 ###
# aby możliwe bylo skorzystanie z pliku testowego, który znajduje sie w innym katalogu, niż testowany plik z kodem
# musimy z poziomu terminala wywołać (zwróć uwagę z poziomu jakiego katalogu wywołujesz!):
# ~/pythonGit/unittest/zadania/testowanie_klas_i_metod$ python -m unittest testCalc/test_calc.py -v


### metoda 2 ###
# procedura dodawania ścieżki do katalogu, w którym python szuka modułów
#   1. Sprawdzenie, jakie katalogi są dodane do przeszukania przez python
'''
odpalamy konsole języka python poleceniem w terminalu: python
>>> import sys
>>> sys.path
['', '/usr/lib/python311.zip', '/usr/lib/python3.11', '/usr/lib/python3.11/lib-dynload', '/usr/local/lib/python3.11/dist-packages', '/usr/lib/python3/dist-packages', '/usr/lib/python3.11/dist-packages']
sys.path - jest to lista ścieżek katalogów, w których python szuka modułów (importów)
'''
#   2. Importujemy moduł systemowy, tworzymy zmienną path zawierającą naszą ścieżkę do dodania i za pomocą append dodajemy ją do sys.path
import sys
path = r'/home/micha/pythonGit/unittest/zadania/testowanie_klas_i_metod'
sys.path.append(path)
#   3. Teraz, aby odpalić plik testowy z innego katalogu niż testowany kod, wystarczy go uruchomić w standardowy sposób będąc w katalogu, w którym on się znajduje
#   ~/pythonGit/unittest/zadania/testowanie_klas_i_metod/testCalc$ python -m unittest test_calc_1.py -v


# działające skrypty testujące te moduły są dostępne w unittest/zadania/
# ~unittest/zadania/testowanie_klas_i_metod/testCalc/test_calc.py, test_calc_1.py