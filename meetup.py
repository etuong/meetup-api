#!/usr/bin/python

import json
import sqlite3


def createdb(db_file_name, json_file_name):
    connection = sqlite3.connect(db_file_name)
    c = connection.cursor()

    with open(json_file_name, "r") as f:
        data = json.load(f)

    customer_set = set()

    order_id = 1
    for order in data['orders']:
        c.execute("INSERT INTO orders (ordersID) VALUES (?)", (order_id,))

        for item in order['items']:
            item_name = item.get('name')
            item_price = item.get('price')
            c.execute("INSERT INTO items (name, price, ordersID) VALUES (?,?,?)", (item_name, item_price, order_id,))

        charges_date = order['charges']['date']
        charges_subtotal = order['charges']['subtotal']
        charges_taxes = order['charges']['taxes']
        charges_total = order['charges']['total']
        charges_formatted_date = "20" + charges_date[6:8] + "-" + charges_date[0:2]+ "-" + charges_date[3:5]
        c.execute("INSERT INTO charges (date, total, subtotal, taxes,ordersID) VALUES (?,?,?,?,?)",
                  (charges_formatted_date, charges_total, charges_subtotal, charges_taxes, order_id,))

        payment_method = order['payment']['method']
        c.execute("INSERT INTO payment (method, ordersID) VALUES (?,?)", (payment_method, order_id,))
        if payment_method == 'credit_card':
            current_payment_id = c.lastrowid
            payment_card_type = order['payment']['card_type']
            payment_last_4_card_number = order['payment']['last_4_card_number']
            payment_zip = order['payment']['zip']
            payment_cardholder = order['payment']['cardholder']

            c.execute("UPDATE payment SET card_type = ? WHERE paymentID = ?",
                      (payment_card_type, current_payment_id))

            if payment_cardholder not in customer_set:
                c.execute("INSERT INTO customers (zip, last_4_card_number, name) VALUES (?,?,?)",
                          (payment_zip, payment_last_4_card_number, payment_cardholder))
                customer_set.add(payment_cardholder)
                customer_id = c.lastrowid
            else:
                customer_id = c.execute('select customersID from customers where name = ?', (payment_cardholder,)).fetchone()[0]

            c.execute("UPDATE payment SET customersID = ? WHERE paymentID = ?",
                          (customer_id, current_payment_id))

        order_id = order_id + 1

    connection.commit()


db_file_name = 'reids.db'
json_file_name = 'reids.json'
createdb(db_file_name, json_file_name)
