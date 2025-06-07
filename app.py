from flask import Flask, render_template, request , flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY']="My Secrete key is no one supposed to know"

#Creating A Class Form Like Login Page
class namerform(FlaskForm):
    name = StringField("What's Your Name: ", validators=[DataRequired()])
    password=PasswordField("Enter your password: ", validators=[DataRequired()])
    submit = SubmitField("submit")


#Creating a Login page
@app.route('/userpage', methods=['GET', 'POST'])
def login_page():
    name = None
    password = None
    form = namerform()
    #validating
    if form.validate_on_submit():
        name = form.name.data
        password =form.password.data
        form.name.data = ''
        form.password.data=''
        flash("Logged-in successfully !!!!")

    return render_template("login_page.html", name = name , form = form , password =password)
       

    



#Using The jInja Properties
@app.route('/')
def homepage():
    stuff="This Some Random shitt!!"
    food=["pizza","samosa","jeraa","vadapav","khachori"]
    return render_template('home_page.html'
                           , stuff=stuff, food=food )


#Using The URL Sytnax
@app.route('/user/<name>')
def next(name):
    return render_template('index.html', username=name)

#Customized Error showing page
@app.errorhandler(404)
def error_page(e):
    return render_template('error.html')      


if __name__ == '__main__':
    app.run(debug=True, port=15000)


