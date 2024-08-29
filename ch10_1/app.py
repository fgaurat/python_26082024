from flask import Flask,render_template
from CustomerDAO import CustomerDAO

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/customers")
def customers():
    # dao = CustomerDAO(r'..\customers.db')# windows
    dao = CustomerDAO(r'../customers.db')
    customers = dao.find_all()
   
    return render_template("customers.html",customers=customers)