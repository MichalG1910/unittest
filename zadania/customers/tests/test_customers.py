import unittest
import psycopg2
import sys
path = r'/home/micha/pythonGit/unittest/zadania/customers'
sys.path.append(path)
from customers_db.customers import CustomersDB


class TestCustomersDB(unittest.TestCase):

    def setUp(self):
        self.connection = psycopg2.connect(database='postgres', user='postgres', password='grabarzmichal1910', host='127.0.0.1', port= '5432')
        self.cursor = self.connection.cursor()
        self.connection.autocommit = True
        self.cursor.execute('''CREATE DATABASE unittest''')
        self.cursor.close()
        self.connection.close()
        
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
        db = CustomersDB(self.connection)
        db.add_customer('Jan', 'Nowak', 'jan.nowak@mail.com', '444', 'Poland')
        self.cursor = self.connection.cursor()

        # act
        self.cursor.execute('''
            SELECT *
            FROM customers
            ORDER BY first_name, last_name;
        ''')
        
        # assert
        expected = (
            ('Jan', 'Nowak', 'jan.nowak@mail.com', '444', 'Poland'),
            ('John', 'Doe', 'john.doe@mail.com', '333', 'USA'),
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
            ('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
        )
        self.assertEqual(tuple(self.cursor), expected)

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