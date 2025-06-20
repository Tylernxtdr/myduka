from flask import Flask,render_template,request,redirect,url_for
from database import get_products,get_sales,insert_products,insert_stock,get_stock,insert_sales

#creating a flask instance
app = Flask(__name__)

# @app.route('/') # decorator function -> can take saome parameters
# def home(): # view function
#     return render_template("index.html")

@app.route('/products') #rule -> defines a path a user accesses in the browser & endpoint - name of view function
def product(): # view function
    products =get_products()
    return render_template("products.html",data = products)


@app.route('/sales')
def sale():
    sales = get_sales()
    products=get_products()
    return render_template("sales.html",data2 = sales,products=products)

@app.route('/')
def dboard():
    db = "My Dashboard"
    return render_template("dashboard.html",data3=db)

@app.route('/login')
def login():
    lg = "Log into your account"
    return render_template("login.html",data4=lg)

@app.route('/register')
def register():
    rg = "Register a new account"
    return render_template("register.html",data5 = rg)

@app.route('/products')
def prod():
    products = get_products()
    return render_template("products.html",data=products)

@app.route('/add_prod',methods=['GET','POST'])
def add_prod():
    product_name = request.form['product_name']
    buying_price = request.form['buying']
    selling_price = request.form['selling']
    new_product = (product_name,buying_price,selling_price)
    insert_products(new_product)
    return redirect(url_for('prod'))


@app.route('/stock')
def stck():
    products = get_products()
    stock=get_stock()
    return render_template("stock.html",products=products,stock=stock)



@app.route('/add_stock', methods=['GET', 'POST'])
def add_stck():
    pid = request.form['pid']
    stock_quantity = request.form['stock']
    new_sale = (pid,stock_quantity)
    insert_sales(new_sale)
    return redirect (url_for('stck')) # pass view function in brackets


@app.route('/add_sale',methods=['GET','POST'])
def add_sale():
    product_id= request.form['product_id']
    quantity = request.form['quantity']
    new_sale = (product_id,quantity)
    insert_sales(new_sale)
    return redirect(url_for('sale'))





app.run(debug=True)
