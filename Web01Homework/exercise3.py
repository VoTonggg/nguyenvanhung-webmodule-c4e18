from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello C4E 18"

@app.route('/user/<username>')
def profile_call(username):
    users = {
        "quy" : {
            "name" : "Dinh Cong Quy",
            "age" : 20,
            "gender" : 1
        },
        "tuananh" : {
            "name" : "Huynh Tuan Anh",
            "age" : 22,
            "gender" : 1
        },
        "hung" : {
            "name" : "Nguyen Van Hung",
            "age" : 22,
            "gender" : 1 
        },
        "giang" : {
            "name" : "Nguyen Thu Giang",
            "age" : 26,
            "gender" : 0
        }
    }
    if username in users:
        user = users[username]
        return render_template("userprofile.html", user = user)
    else:
        return "<b> User not found </b>"

if __name__ == '__main__':
  app.run(debug=True)
 