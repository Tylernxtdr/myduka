from flask import Flask

#creating a flask instance
app = Flask(__name__)

@app.route('/') # decorator function -> can take saome parameters
def home(): # view function
    return "Trevor Tyler"

@app.route('/name') #rule -> defines a path a user accesses in the browser
def name(): # view function
    return "My name is Tyler"

app.run(debug=True)  # watcher - checkig for any changes in an application and reloading it  

# # TASK 
#1. Create 3 routes and return 3 different data values and test them in yur browser
@app.route('/num0')
def fun1():
    return "PRODUCT1"

@app.route('/num1')
def fun2():
    return "PRODUCT2"

@app.route('/num2')
def fun3():
    return "PRODUCT3"

app.run(debug=True)
#2. In your project folder create 2 folders :
   # a) templates
   # b) static
