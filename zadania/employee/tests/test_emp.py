import unittest
import sys
path = r'/home/micha/pythonGit/unittest/zadania/employee'
sys.path.append(path)
from employee.emp import Employee





class TestEmployee(unittest.TestCase):
    
    def setUp(self) :
        print(f'setting up...')
        self.emp = Employee('John', 'Smith', 80000)    
    def tearDown(self) :
        print(f'tearig down ...')
        del self.emp


    def test_email(self):
        self.assertEqual(self.emp.email, 'john.smith@mail.com')
    
    def test_email_after_changing_first_name(self):
        self.emp.first_name = 'Michal'
        self.assertEqual(self.emp.email, 'michal.smith@mail.com')
        
    
    def test_email_after_changing_last_name(self):
        self.emp.last_name = 'Grabarz'
        self.assertEqual(self.emp.email, 'john.grabarz@mail.com')
        
    def test_tax(self):
        self.assertEqual(self.emp.tax, 13600.0)
    
    def test_salary_after_applying_bonus(self):
        self.emp.apply_bonus()
        self.assertEqual(self.emp.salary, 88000)
        
        

if __name__ == '__main__':
    unittest.main(verbosity=2)