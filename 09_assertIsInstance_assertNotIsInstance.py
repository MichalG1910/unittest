import unittest

# asssertIsInstance(obiekt,klasa) - jeśli obiekt(klasa) jest instancją klasy to test OK
# asssertNotIsInstance(obiekt,klasa) - jeśli obiekt(klasa)  nie jest instancją klasy to test OK

class Person:
    def __init__(self,name):
        self.name = name

class Worker(Person):
    pass 

class TestPerson(unittest.TestCase):
    
    # sprawdzamy, czy klasa Person jest instancją klasy type (type - każda klasa ma typ type)
    def test_case_1(self):
        self.assertIsInstance(Person, type)
    def test_case_2(self):
        person = Person('Adam')
        self.assertIsInstance(person, Person)

class TestWorker(unittest.TestCase):

    def test_case_3(self):
        worker = Worker('Filip')
        self.assertIsInstance(worker, Worker)
    def test_case_4(self):
        worker = Worker('Filip')
        self.assertIsInstance(worker, Person)
    def test_case_5(self):
        self.assertIsInstance(Worker, Person)
    def test_case_6(self):
        self.assertNotIsInstance(Worker, Person)
    def test_case_7(self):
        self.assertNotIsInstance(6, int)
    def test_case_8(self):
        self.assertNotIsInstance(0.6, int)
    


if __name__ == '__main__':
    unittest.main(verbosity=2)



'''
test_case_1 (__main__.TestPerson.test_case_1) ... ok
test_case_2 (__main__.TestPerson.test_case_2) ... ok
test_case_3 (__main__.TestWorker.test_case_3) ... ok
test_case_4 (__main__.TestWorker.test_case_4) ... ok
test_case_5 (__main__.TestWorker.test_case_5) ... FAIL
test_case_6 (__main__.TestWorker.test_case_6) ... ok
test_case_7 (__main__.TestWorker.test_case_7) ... FAIL
test_case_8 (__main__.TestWorker.test_case_8) ... ok

======================================================================
FAIL: test_case_5 (__main__.TestWorker.test_case_5)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/micha/pythonGit/unittest/09_assertIsInstance_assertNotIsInstance.py", line 28, in test_case_5
    self.assertIsInstance(Worker, Person)
AssertionError: <class '__main__.Worker'> is not an instance of <class '__main__.Person'>

======================================================================
FAIL: test_case_7 (__main__.TestWorker.test_case_7)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/micha/pythonGit/unittest/09_assertIsInstance_assertNotIsInstance.py", line 32, in test_case_7
    self.assertNotIsInstance(6, int)
AssertionError: 6 is an instance of <class 'int'>

----------------------------------------------------------------------
Ran 8 tests in 0.001s

FAILED (failures=2)
'''