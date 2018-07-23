from flask import *
from models.service import Service
from models.user import User
import mlab

app = Flask(__name__)
app.secret_key = "a super super secret key"

mlab.connect()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    all_service = Service.objects()
    return render_template('search.html', all_service = all_service)

@app.route('/detail/<service_id>')
def detail(service_id):
    service = Service.objects().with_id(service_id)
    return render_template('service_detail.html', service = service)

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
        return render_template("newservice.html") 
    elif request.method == "POST":
        form = request.form
        new_service = Service(
            name = form['name'],
            yob = form['yob'],
            gender = form['gender'],
            height = form['height'],
            phone = form['phone'],
            address = form['address'],
            description = form['description'],
            measurements = form['measurements'],
            image = form['image'],
            status = form['status']
        )
        new_service.save()
        return redirect(url_for('admin'))

@app.route('/update-service/<service_id>', methods = ["GET", "POST"])
def updateservice(service_id):
    if request.method == "GET":
        service = Service.objects().with_id(service_id)
        return render_template('updateservice.html', service = service)
    else:
        form = request.form
        service = Service.objects().with_id(service_id)
        service.update(
            set__name = form['name'],
            set__yob = form['yob'],
            set__gender = form['gender'],
            set__height = form['height'],
            set__phone = form['phone'],
            set__address = form['address'],
            set__description = form['description'],
            set__measurements = form['measurements'],
            set__image = form['image'],
            set__status = form['status']
        )
        service.reload()
        return redirect(url_for('admin'))

@app.route('/sign-up', methods = ["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template('signup.html')
    else:
        form = request.form 

        newuser = User(
            username = form['username'],
            password = form['password'],
            email = form['email'],
            fullname = form['fullname']
        )
        newuser.save()
        return redirect(url_for('index'))

@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        form = request.form
        username = form['username']
        password = form['password']

        user_to_find = User.objects(username = username, password = password)
        if user_to_find is not None:
            session['loggedin'] = True
            return user_to_find
        else:
            return "Log in failed"

if __name__ == '__main__':
  app.run(debug=True)
 