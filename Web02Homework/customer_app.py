from flask import Flask, render_template
from models.customer import Customer
import mlab
app = Flask(__name__)

mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customer')
def customer():
    all_customer = Customer.objects(contacted = False, gender = 1)
    if len(all_customer) < 10:
        first_ten_cust = all_customer
    else:
        first_ten_cust = all_customer[0:10]
    return render_template('customer.html', first_ten_cust = first_ten_cust)


if __name__ == '__main__':
  app.run(debug=True)
 