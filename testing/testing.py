#!/usr/bin/env python

from aflaskapp import app
import unittest
import json

class ApiTestCase(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        self.app.testing = True
        pass

    def tearDown(self):
        pass

    def test_list_customers(self):
        list_customer_result = self.app.get('/customers')
        self.assertEqual(list_customer_result.status_code, 200)
        data = json.loads(list_customer_result.data)
        self.assertEqual(3, len(data))

    def test_get_valid_customer(self):
        get_customer_result = self.app.get('/customers/111')
        self.assertEqual(get_customer_result.status_code, 200)
        data = json.loads(get_customer_result.data)
        self.assertIsNotNone(data)

    def test_get_invalid_customer(self):
        get_customer_result = self.app.get('/customers/foo')
        self.assertEqual(get_customer_result.status_code, 404)

    def test_list_valid_customer_accounts(self):
        customer_accounts_result = self.app.get('/customers/111/accounts')
        self.assertEqual(customer_accounts_result.status_code, 200)
        data = json.loads(customer_accounts_result.data)
        self.assertEqual(3, len(data))

    def test_list_invalid_customer_accounts(self):
        customer_accounts_result = self.app.get('/customers/foo/accounts')
        self.assertEqual(customer_accounts_result.status_code, 404)

    def test_get_valid_customer_account(self):
        customer_account_result = self.app.get('/customers/111/accounts/1')
        self.assertEqual(customer_account_result.status_code, 200)
        data = json.loads(customer_account_result.data)
        self.assertEqual('1', data['id'])
        self.assertEqual('11112222', data['data']['account_number'])

    def test_get_valid_customer_invalid_account(self):
        customer_account_result = self.app.get('/customers/111/accounts/7')
        self.assertEqual(customer_account_result.status_code, 404)

    def test_get_invalid_customer_account(self):
        customer_account_result = self.app.get('/customers/foo/accounts/7')
        self.assertEqual(customer_account_result.status_code, 404)

if __name__ == "__main__":
    unittest.main()
