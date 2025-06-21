
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
    # profit per day

def get_sales_per_product():
    cur.execute(""" Select products.name , sum(sales.quantity * products.selling_price)
                 as revenue from products join sales on products.id = sales.pid group by (products.name); """)
    sale_per_prod = cur.fetchall()
    return sale_per_prod

def get_profit_per_prod():
    cur.execute(""" Select name , sum(quantity * (selling_price - buying_price)) as profit_per_prod from products
                 join sales on products.id=sales.pid group by name;
                 """)
    profit_per_prod = cur.fetchall()
    return profit_per_prod

def get_sales_per_day():
    cur.execute("""Select sum(quantity * selling_price),created_at from products
                 join sales on products.id = sales.pid group by created_at;
        """)
    sale_per_day = cur.fetchall()
    return sale_per_day

def profit_per_day():
    cur.execute("""Select sum(selling_price - buying_price),created_at from products
                 join sales on products.id = sales.pid group by created_at;
            """)
    profit_per_day = cur.fetchall()
    return profit_per_day