from flask import Flask,render_template
from database import get_products,get_sales

#creating a flask instance
app = Flask(__name__)

# @app.route('/') # decorator function -> can take saome parameters
# def home(): # view function
#     return render_template("index.html")

@app.route('/') #rule -> defines a path a user accesses in the browser & endpoint - name of view function
def product(): # view function
    products =get_products()
    return render_template("products.html",data = products)


@app.route('/sales')
def sale():
    sales = get_sales()
    return render_template("sales.html",data2 = sales)

@app.route('/dashboard')
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


app.run(debug=True)
