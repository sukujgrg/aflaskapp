#!/usr/bin/env python

from flask import Flask, jsonify

app = Flask(__name__)

ACCOUNTS = {
    '111' : {
        '1' : {'bsb': '060-000', 'account_number': '11112222', 'type': 'tx', 'alias': 'Transaction Account', 'balance': 1000.00},
        '2' : {'bsb': '060-111', 'account_number': '22223333', 'type': 'm', 'alias': 'Mortgage', 'balance': -350000.00},
        '3' : {'account_number': '4532070810616690', 'type': 'cc', 'alias': 'Credit Card', 'balance': 500.00}
    },
    '222' : {
        '4' : {'bsb': '060-222', 'account_number': '33334444', 'type': 'tx', 'alias': 'Transaction Account', 'balance': 25.00}
    },
    '333' : {
        '5' : {'account_number': '5274393383004246', 'type': 'cc', 'alias': 'Credit Card', 'balance': 3592.22}
    },
}
CUSTOMERS = {
    '111' : {'name': 'Deadpool'},
    '222' : {'name': 'Daredevil'},
    '333' : {'name': 'Captain America'},
}

@app.route('/customers', methods=['GET'])
def list_customers():
    return jsonify([{'id': key, 'data': CUSTOMERS[key]} for key in CUSTOMERS.keys()])

@app.route('/customers/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    if customer_id not in CUSTOMERS:
        return jsonify({'error': 'Customer %s does not exist' % customer_id}), 404

    return jsonify({'id': customer_id, 'data': CUSTOMERS[customer_id]})

@app.route('/customers/<customer_id>/accounts', methods=['GET'])
def list_customer_accounts(customer_id):
    if customer_id not in CUSTOMERS:
        return jsonify({'error': 'Customer %s does not exist' % customer_id}), 404

    return jsonify([{'id': key, 'data': ACCOUNTS[customer_id][key]} for key in ACCOUNTS[customer_id].keys()])

@app.route('/customers/<customer_id>/accounts/<account_id>', methods=['GET'])
def get_customer_account(customer_id, account_id):
    if customer_id not in CUSTOMERS:
        return jsonify({'error': 'Customer %s does not exist' % customer_id}), 404
    if account_id not in ACCOUNTS[customer_id]:
        return jsonify({'error': 'Account %s for customer %s does not exist' % (account_id, customer_id)}), 404

    return jsonify({'id': account_id, 'data': ACCOUNTS[customer_id][account_id]})

if __name__ == "__main__":
    app.run(host='0.0.0.0')
