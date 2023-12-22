#!/usr/bin/env python3

from flask import Flask, request, jsonify
import configuration as conf
import logging

app = Flask('Credit Policy Service - CPS')


def check_credit_policy(request_data):
    """
    This function checks if the credit policy is respected
    """
    logging.debug(f"Request data : {request_data}")

    # Checking that the request data has the right format
    if not set(request_data.keys()) == set(conf.REQUEST_KEYS):
        raise ValueError(f'Requests the have the following format : {conf.REQUEST_FORMAT_ERROR}')

    customer_income, customer_debt, payment_remarks_12m, payment_remarks, customer_age = [request_data[k]
                                                                                          for k in conf.REQUEST_KEYS]

    # Income check
    if customer_income < 500:
        return conf.STATUS_REJECT, 'LOW_INCOME'

    # Debt check
    if customer_debt > 0.5 * customer_income:
        return conf.STATUS_REJECT, 'HIGH_DEBT_FOR_INCOME'

    # Payment remarks check
    if payment_remarks_12m > 0:
        return conf.STATUS_REJECT, 'PAYMENT_REMARKS_12M'

    if payment_remarks > 1:
        return conf.STATUS_REJECT, 'PAYMENT_REMARKS'

    # Age check
    if customer_age < 18:
        return conf.STATUS_REJECT, 'UNDERAGE'

    # All checks passed
    return conf.STATUS_ACCEPT, None


@app.route('/check_credit_policy', methods=['POST'])
def evaluate_credit_policy():
    try:
        request_data = request.json
        result, reason = check_credit_policy(request_data)
        response = {'result': result, 'reason': reason}
        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    logging.basicConfig(level='INFO')

    app.run(debug=True)
