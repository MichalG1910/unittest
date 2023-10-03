import unittest
from parameterized import parameterized 
import sys
path = r'/home/micha/pythonGit/unittest/zadania/shopping_basket'
sys.path.append(path)
from shopping.basket import ShoppingBasket


class TestShoppingBasketWithNoProducts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n[INFO] Setting up basket without any product...')
        cls.basket = ShoppingBasket()
        #cls.basket.add_product('milk', 2)
    def test_size_of_basket_should_be_empty(self):
        self.assertEqual(len(self.basket), 0)               # len(self.basket) - możliwy taki zapis, ponieważ używamy w klasie basket metody magucznej __len__

    def test_getting_product_out_of_range_should_raise_error(self):
        self.assertRaises(IndexError, self.basket.get_product, 0)

    def test_total_amount_should_be_zero(self):
        self.assertEqual(self.basket.total(),0)


class TestShoppingBasketWithOneProduct(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n[INFO] Setting up basket with one product...')
        cls.basket = ShoppingBasket().add_product('milk', 3.0)

    def test_size_of_basket_should_be_one(self):
        self.assertEqual(len(self.basket),1)            # self.assertEqual(self.basket.__len__(), 1)

    def test_total_amount_should_have_tax(self):
        self.assertEqual(self.basket.total(10), 3.3)

    def test_getting_product(self):
        self.assertEqual(self.basket.get_product(0).name, 'milk')
    
    def test_getting_product_moje_rozwiazanie(self):
        self.assertIn('milk', (product.name for  product in self.basket.products))

    def test_getting_product_out_of_range_should_raise_error(self):
        self.assertRaises(IndexError, self.basket.get_product, 1)


class TestShoppingBasketWithTwoProducts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n[INFO] Setting up basket with two products...')
        cls.basket = ShoppingBasket() \
            .add_product('milk', 3.0) \
            .add_product('water', 2.0) \
        # wyżej ciekawy sposób na stworzenie obiektu i jednoczesne użycie jego metod w celu utworzenia produktów w naszym koszyku

    def test_size_of_basket_should_be_two(self):
        self.assertEqual(len(self.basket),2)
    
    @parameterized.expand([(0, 'milk'),(1, 'water')])               # skorzystałem z testów parametryzowanych, aby wykonało wszystkie 
    def test_order_of_products_name(self, index, name):             # przypadki. W tutorialu tak nie zrobiono (nie było to konieczne)
        self.assertEqual(self.basket.get_product(index).name, name)
    
    @parameterized.expand([(0, 3.0),(1, 2.0)])
    def test_order_of_products_price(self, index, price):
        self.assertEqual(self.basket.get_product(index).price, price)

    def test_total_amount_should_have_tax(self):
        self.assertEqual(self.basket.total(), 6.05)

    def test_getting_product_out_of_range_should_raise_error(self):
        self.assertRaises(IndexError, self.basket.get_product, 2)
    
if __name__ == '__main__':
    unittest.main(verbosity=2)


'''
[INFO] Setting up basket without any product...
test_getting_product_out_of_range_should_raise_error (__main__.TestShoppingBasketWithNoProducts.test_getting_product_out_of_range_should_raise_error) ... ok
test_size_of_basket_should_be_empty (__main__.TestShoppingBasketWithNoProducts.test_size_of_basket_should_be_empty) ... ok
test_total_amount_should_be_zero (__main__.TestShoppingBasketWithNoProducts.test_total_amount_should_be_zero) ... ok

[INFO] Setting up basket with one product...
test_getting_product (__main__.TestShoppingBasketWithOneProduct.test_getting_product) ... ok
test_getting_product_moje_rozwiazanie (__main__.TestShoppingBasketWithOneProduct.test_getting_product_moje_rozwiazanie) ... ok
test_getting_product_out_of_range_should_raise_error (__main__.TestShoppingBasketWithOneProduct.test_getting_product_out_of_range_should_raise_error) ... ok
test_size_of_basket_should_be_one (__main__.TestShoppingBasketWithOneProduct.test_size_of_basket_should_be_one) ... ok
test_total_amount_should_have_tax (__main__.TestShoppingBasketWithOneProduct.test_total_amount_should_have_tax) ... ok

[INFO] Setting up basket with two products...
test_getting_product_out_of_range_should_raise_error (__main__.TestShoppingBasketWithTwoProducts.test_getting_product_out_of_range_should_raise_error) ... ok
test_order_of_products_name_0 (__main__.TestShoppingBasketWithTwoProducts.test_order_of_products_name_0) ... ok
test_order_of_products_name_1 (__main__.TestShoppingBasketWithTwoProducts.test_order_of_products_name_1) ... ok
test_order_of_products_price_0 (__main__.TestShoppingBasketWithTwoProducts.test_order_of_products_price_0) ... ok
test_order_of_products_price_1 (__main__.TestShoppingBasketWithTwoProducts.test_order_of_products_price_1) ... ok
test_size_of_basket_should_be_two (__main__.TestShoppingBasketWithTwoProducts.test_size_of_basket_should_be_two) ... ok
test_total_amount_should_have_tax (__main__.TestShoppingBasketWithTwoProducts.test_total_amount_should_have_tax) ... ok

----------------------------------------------------------------------
Ran 15 tests in 0.000s

OK
'''

