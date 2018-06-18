from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    posts = [
        {
            "title" : "Thơ con ếch",
            "content" : "Hôm nay trăng lên cao quá Anh muốn hôn em vào má",
            "author" : "Tuấn Anh",
            "gender" : 1
        },
        {
            "title" : "Khô Khan",
            "content" : "Hôm nay trăng mới nhú thôi",
            "author" : "Hùng",
            "gender" : 1
        },
        {
            "title" : "God",
            "content" : "Lạy chúa trên cao Turn down for what",
            "author" : "Thu Giang",
            "gender" : 0
        }

    ]
    return render_template("index.html", posts = posts)

@app.route("/hello")
def say_hello():
    return "Hello C4E 18"

@app.route('/sayhi/<name>/<age>')
def say_hi(name, age):
    return "Hi {0}, you're {1} years old".format(name, age)

@app.route('/sum/<int:param1>/<int:param2>')
def addition(param1, param2):
    return str(param1 + param2)

if __name__ == '__main__':
  app.run(debug=True)
 