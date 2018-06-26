import mlab
from models.service import Service
from flask import *


app = Flask(__name__)

# 0. Create connection
mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<gender>')
def search(gender):
    all_service = Service.objects(gender = gender)
    return render_template('search.html', all_service = all_service)

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html', all_service = all_service)

@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_del = Service.objects().with_id(service_id)
    if service_to_del is not None:
        service_to_del.delete()
        return redirect(url_for('admin'))
    else:
        return "Service not found"

@app.route('/newservice', methods = ["GET", "POST"])
def newservice():
    if request.method == "GET":
        return render_template('newservice.html')
    elif request.method == "POST":
        form = request.form 
        name = form['name']
        yob = form['yob']
        address = form['address']

        new_service = Service(
            name = name,
            yob = yob,
            address = address
        )
        new_service.save()

        return name + yob + address
        
        

if __name__ == '__main__':
  app.run(debug=True)

