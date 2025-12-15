import pandas as pd
import psycopg2
import pandas

import random
from password import password


def generate_order_history():
    conn = psycopg2.connect(
        host='localhost',
        database='postgres',
        user='postgres',
        password=password,
        port='5432'
    )

    cur = conn.cursor()

    gather_orders_query = 'SELECT * FROM orders'

    cur.execute(gather_orders_query)

    orders_data = cur.fetchall()

    gather_product_query = 'SELECT * FROM Products'

    cur.execute(gather_product_query)

    product_data = cur.fetchall()



    order_history = []
    for index,order in enumerate(orders_data):
        product_purchased = []
        price = 0.00
        # 10 randomly purchased products that will be used in forloop
        random_amount_purchase = random.randint(1,10)
        order_index = index
        order_id = order[0]
        # print(order_id,order)
        for purchase_index in range(random_amount_purchase):
            random_product = random.choice(product_data)
            product_purchased.append([random_product[0]])
            price += random_product[3]
        order_history.append([index+1,order_id,product_purchased,len(product_purchased),round(price, 2)])
    # pd.DataFrame(order_history).to_csv('output_example.csv')

    return(order_history)


if __name__ == '__main__':
    data = generate_order_history()

    # data = pd.DataFrame(data, columns=['orderDetails','orderid','customereid','date'])

    # print(data)

