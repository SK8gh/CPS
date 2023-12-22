#!/usr/bin/env python3

"""
Project configuration
"""

# Expected request format (storing the expected types as well)
REQUEST_KEYS = ['customer_income', 'customer_debt', 'payment_remarks_12m', 'payment_remarks', 'customer_age']

REQUEST_FORMAT_ERROR = """
{'customer_income': ... ,
 'customer_debt': ... ,
 'payment_remarks_12m': ... ,
 'payment_remarks': ... ,
 'customer_age': ...
}
"""

STATUS_REJECT = 'REJECT'

STATUS_ACCEPT = 'ACCEPT'
