
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


# product_values1 = ('shoes',1500,3000)
# product_values2 = ('phone',30000,50000)

# insert_products(product_values1)
# insert_products(product_values2)


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

stock = get_stock()
print(stock)