#!/usr/bin/env python3

from CREDIT_SERVICE import check_credit_policy
import configuration as conf
import unittest
import logging


class TestCreditPolicy(unittest.TestCase):
    def test_valid_request(self):
        test_data = {
            'customer_income': 10000,
            'customer_debt': 0,
            'payment_remarks_12m': 0,
            'payment_remarks': 0,
            'customer_age': 99
        }

        result, reason = check_credit_policy(test_data)
        self.assertEqual(result, conf.STATUS_ACCEPT)
        self.assertIsNone(reason)


if __name__ == '__main__':
    logging.basicConfig(level='DEBUG')

    unittest.main()
