
import unittest
from app import add, Customer
class AppTestCases(unittest.TestCase):
    def test_positive_int_int(self):
        actual = add(1,2)
        expected = 3
        self.assertEqual(actual, expected)

    def test_positive_int_float(self):
        actual = add(1,2.5)
        expected = 3.5
        self.assertEqual(actual, expected)

    # def test_positive_int_str(self):
    #     actual = add(1,"2.5")
    #     expected = None
    #     self.assertEqual(actual, expected)

class CustomerTescases(unittest.TestCase):

    # def setUp(self):
    #     print("setting up data")
    #     self.cust = Customer(1,"cust1")

    # def tearDown(self):
    #     print("UNALLOCATING RESOURCES CREATED IN SETUP")
    #     self.cust=None

    def test_1create(self):
        print("executing create")
        act = self.cust.create_customer()
        expected = "created"
        self.assertEqual(expected, act)

    def test_2update(self):
        print("executing update")
        act = self.cust.update_customer()
        expected = "updated"
        self.assertEqual(expected, act)

    def test_3delete(self):
        print("executing delete")
        act = self.cust.delete_customer()
        expected = "deleted"
        self.assertEqual(expected, act)

    @classmethod
    def setUpClass(cls):
        print("seeting up data")
        cls.cust=Customer(1,"cust1")

    @classmethod 
    def tearDownClass(cls):
        print("UNALLOCATING RESOURCES")
        cls.cust=None

#unittest.main()
