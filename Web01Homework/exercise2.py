

# Not using render_template() function
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello C4E 18"

@app.route('/bmi/<int:weight>/<int:height>')
def bmi_calc(weight, height):
    bmi_result = weight / ((height / 100) ** 2)
    if bmi_result < 16:
        return "Your BMI result: " + str(bmi_result) + " Your status : Severely underweight"
    elif bmi_result < 18.5:
        return "Your BMI result: " + str(bmi_result) + " Your status : Underweight"
    elif bmi_result < 25:
        return "Your BMI result: " + str(bmi_result) + " Your status : Normal"
    elif bmi_result < 30:
        return "Your BMI result: " + str(bmi_result) + " Your status : Overweight"
    else:
        return "Your BMI result: " + str(bmi_result) + " Your status : Obese"

if __name__ == '__main__':
  app.run(debug=True)
 

# Using render_template() function
# from flask import Flask, render_template
# app = Flask(__name__)


# @app.route('/')
# def index():
#     return "Hello C4E 18"

# @app.route('/bmi/<int:weight>/<int:height>')
# def bmi_calc(weight, height):
#     bmi_result = weight / ((height / 100) ** 2)
#     if bmi_result < 16:
#         bmi_status = "Severely underweight"
#     elif bmi_result < 18.5:
#         bmi_status = "Underweight"
#     elif bmi_result < 25:
#         bmi_status = "Normal"
#     elif bmi_result < 30:
#         bmi_status = "Overweight"
#     else:
#         bmi_status = "Obese"
#     return render_template("bmicalculation.html", bmi_result = bmi_result, bmi_status = bmi_status)
# if __name__ == '__main__':
#   app.run(debug=True)