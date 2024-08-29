from flask import Flask
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
    html = "<h1>Customers</h1><table>"


    for customer in customers:
        html += f"""
<tr>
    <td>{customer.id}</td>
    <td>{customer.first_name}</td>
    <td>{customer.last_name}</td>
    <td>{customer.email}</td>
    <td>{customer.gender}</td>
</tr>
        """
    html+= "</table>"
    return html