
import psycopg2

conn = psycopg2.connect(user="postgres",password="Gianna@184",host="localhost",port="5432",database="myduka")

cur = conn.cursor()

def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products



cur.execute("insert into products(name,buying_price,selling_price)values('eggs',12,15)")
conn.commit()



def insert_products(values) :
    insert_query = "insert into products(name,buying_price,selling_price)values(%s,%s,%s)"
    cur.execute(insert_query,values)
    conn.commit()



def get_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales



def insert_sales(values):
    insert_sales = "insert into sales(pid,quantity,created_at)values(%s,%s,now())"
    cur.execute(insert_sales,values)
    conn.commit()


def insert_stock(values):
    insert_stock = "insert into stock(pid,stock_quantity,created_at)values(%s,%s,now())"
    cur.execute(insert_stock,values)
    conn.commit()


def get_stock():
    cur.execute ("Select * from stock;")
    stock = cur.fetchall()
    return stock



# Attempt to update stock after making a sale
# only make sales if you have enough stock
# write the following  sql queries:
    # sales per day
    # sales per product
    # profit per day
    # profit per product