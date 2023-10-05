import unittest
import psycopg2


# Struktura testu - wzorzec AAA (Arrange-Act-Assert) - w przypadku bardziej skomplikowanych testów pozwala lepiej uporządkować testy 
# Arrange - zaaranżowanie danych wejściowych i warunków wstępnych
# Act - działanie na funkcji/metodzie/klasie
# Assert - dokonanie asercji

class CustomersDB:

    def __init__(self, connection):
        self.connection = connection

    def add_customer(self,first_name,last_name,email,phone,country):
        add_list = (first_name, last_name, email, phone, country)
        
        cursor = self.connection.cursor()
        sql = '''
            INSERT INTO customers (first_name, last_name, email, phone, country)
            VALUES (%s, %s, %s, %s, %s);'''
        cursor.execute(sql, add_list)
        self.connection.commit()
        return cursor.lastrowid

    def find_customers_by_first_name(self, first_name):
        cursor = self.connection.cursor()
        sql = f'''
            SELECT *
            FROM customers
            WHERE first_name LIKE '{first_name}'
            ORDER BY first_name, last_name;'''
        cursor.execute(sql)
        for row in cursor:  # iterujemy po obiekcie cursor 
            yield row       # i zwracamy kazdy wiersz z danymi, jaki zawiera
            

    def find_customers_by_country(self, country):
        cursor = self.connection.cursor()
        sql = f'''
            SELECT *
            FROM customers
            WHERE country LIKE '{country}'
            ORDER BY first_name, last_name;'''
        cursor.execute(sql)
        for row in cursor:
            yield row


class TestCustomersDB(unittest.TestCase):

    # używając parametryzacji na poziomie test_case  przygotowujemy (setUp) środowisko do testów i sprzątamy (tearDown) je po wykonaniu test_case
    def setUp(self): 
        # tworzymy połączenie do DB postgres(baza pozwoli nam utworzyć DB unittest) i tworzymy DB unittest. Po tej operacji kończymy połączenie zDB postgres
        self.connection = psycopg2.connect(database='postgres', user='postgres', password='grabarzmichal1910', host='127.0.0.1', port= '5432')
        self.cursor = self.connection.cursor()
        self.connection.autocommit = True
        self.cursor.execute('''CREATE DATABASE unittest''')
        self.cursor.close()
        self.connection.close()
        
        # tworzymy połączenie z nowo utworzoną DB unittest, tworzymy w niej tabelę customers i wypelniamy ją danymi
        self.connection = psycopg2.connect(database='unittest', user='postgres', password='grabarzmichal1910', host='127.0.0.1', port= '5432')
        self.cursor = self.connection.cursor()
        create_table_sql = '''
            CREATE TABLE IF NOT EXISTS customers 
            ( 
                first_name TEXT, 
                last_name  TEXT, 
                email      TEXT, 
                phone      TEXT, 
                country    TEXT 
            );'''
        self.cursor.execute(create_table_sql)

        customers_data = [
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
            ('John', 'Doe', 'john.doe@mail.com', '333', 'USA'),
            ('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
        ]

        insert_sql = """
            INSERT INTO customers (first_name, last_name, email, phone, country)
            VALUES (%s, %s, %s, %s, %s);"""
        self.cursor.executemany(insert_sql, customers_data)
        
    def tearDown(self):
        # aby usunąć DB unittest, musimy z niej wyjść i zalogować sie na inną DB (najlepiej postgres). 
        # Po operacji usunięcia DB unittest, zrywamy połączenie z DB postgres
        self.cursor.close()
        self.connection.close()
        self.connection = psycopg2.connect(database='postgres', user='postgres', password='grabarzmichal1910', host='127.0.0.1', port= '5432')
        self.cursor = self.connection.cursor()
        self.connection.autocommit = True
        self.cursor.execute('''DROP DATABASE unittest''')
        self.cursor.close()
        self.connection.close()

    def test_add_customer(self):
        # arrange
        db = CustomersDB(self.connection)                                       # tworzymy obiekt na klasie CustomerDB i przekazujemy do niego nasze połączenie do DB
        db.add_customer('Jan', 'Nowak', 'jan.nowak@mail.com', '444', 'Poland')  # używając metody add_customer dodajemy rekord do DB
        self.cursor = self.connection.cursor()                                  # tworzymy obiekt typu cursor - pozwolo nam to wykonywać zapytania do DB w SQL

        # act (przy użyciu obiektu cursor metodą execute wykonujemy zapytanie Select do DB)
        self.cursor.execute('''                                                 
            SELECT *
            FROM customers
            ORDER BY first_name, last_name;
        ''')
        
        # assert
        expected = (                                                    # tupla, która przechowuje spodziewany przez nas wynik assertEqual
            ('Jan', 'Nowak', 'jan.nowak@mail.com', '444', 'Poland'),
            ('John', 'Doe', 'john.doe@mail.com', '333', 'USA'),
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
            ('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
        )
        self.assertEqual(tuple(self.cursor), expected)                  # dokonujemy assertEqual na obiekcie self.cursor (musimy z niego zrobić tuple, by dało się go porównać z spodziewanym wynikiem expected)

    def test_find_customers_by_first_name(self):
        # arrange
        db = CustomersDB(self.connection)

        # act
        actual = tuple(db.find_customers_by_first_name('John'))

        # assert
        expected = (
            ('John', 'Doe', 'john.doe@mail.com', '333', 'USA'),
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA')
        )
        self.assertEqual(actual, expected)

    def test_find_customers_by_country(self):
        # arrange
        db = CustomersDB(self.connection)

        # act
        actual = tuple(db.find_customers_by_country('USA'))

        # assert
        expected = (
            ('John', 'Doe', 'john.doe@mail.com', '333', 'USA'),
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
            ('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
        )
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)