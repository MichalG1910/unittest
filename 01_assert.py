# Instrukcja assert - zwraca błąd asercji jesli jest False, nie zwraca nic, jesli True (kod jest poprawny)
assert True                     # 
assert -0.4                     # każda liczba inna niż 0 jest True
assert [[]]                     # lista zawierająca 1 element(nawet pustą inna listę) jest True
#assert False, 'dferferferfer'   # AssertionError: dferferferfer        , po ',' możemy dodać komunikat, który zostanie wyświetlony w konsoli
#assert 0                        # AssertionError       
#assert []                       # AssertionError    
 

condition = True            # jeżeli jest True, nie ma AssertionError. Jeśli zmienimy na condition = False, otrzymamy bląd
if not condition:
    raise AssertionError('Assertion message.')
# poniżej skrócony zapis rownoznaczny z tym powyżej
assert condition, 'Assertion message.'


amount = 1000
tax_rate = 0.15
assert amount >=0 , 'The amount should not be negative'
assert 0 < tax_rate < 1, 'Tax rate should be between 0 and 1'
# jeśli amount, tax_rate są True, nie ma błędu. Jak je zmienimy, aby były False:
amount = -1000          # AssertionError: The amount should not be negative   
tax_rate = 1.15         # AssertionError: Tax rate should be between 0 and 1


# funkcja liczy pole prostokąta
def area(widht, height):
    return widht * height
assert area(4,5) == 20          # sprawdzamy asercję poprzez wywołanie funkcji i porównanie jej z poprawnym wynikiem

# poniżej ta sama funkcja z błędem (return widht * height + 1)
def area(widht, height):
    return widht * height + 1
assert area(4,5) == 20          # AssertionError
# tworząc asercję możemy sprawdzic podstawowe założenia dzialania takiej funkcji, jak w tym przypadku czy
# poprawnie liczy pole prostokąta. Jesli w kod wkradł sie błąd, ktorego nie widzi edytor, to taka asercja pozwoli nam go znaleźć



