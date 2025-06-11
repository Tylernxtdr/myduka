
import psycopg2

conn = psycopg2.connect(user="postgres",password="Gianna@184",host="localhost",port="5432",database="myduka")

cur = conn.cursor()

def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products

product_data = get_products()
print(product_data)

cur.execute("insert into products(name,buying_price,selling_price)values('eggs',12,15)")
conn.commit()

product_data = get_products()
print(product_data)

def insert_products(values) :
    insert_query = "insert into products(name,buying_price,selling_price)values(%s,%s,%s)"
    cur.execute(insert_query,values)
    conn.commit()


product_values1 = ('shoes',1500,3000)
product_values2 = ('phone',30000,50000)

insert_products(product_values1)
insert_products(product_values2)

products = get_products()
print(products)

def get_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales

product_data = get_sales()
print(product_data)

def insert_sales(values):
    insert_query = "insert into sales(pid,quantity,created_at)values(%s,%s,%s)"
    cur.execute(insert_query,values)
    conn.commit()

sales1 = (1,300,'now{}')
sales2 = (2,100,'now{}')

insert_sales(sales1)
insert_sales(sales2)


sales = get_sales()
print(sales)