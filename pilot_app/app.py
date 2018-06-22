import mlab
from models.service import Service
from flask import Flask, render_template

app = Flask(__name__)

# 0. Create connection
mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<gender>')
def search(gender):
    all_service = Service.objects(gender = gender, yob__lte = 1998,address__icontains="Hà Nội")
    return render_template('search.html', all_service = all_service)



if __name__ == '__main__':
  app.run(debug=True)

