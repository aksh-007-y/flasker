from flask import Flask, render_template

app = Flask(__name__)


#Using The jInja Properties
@app.route('/')
def homepage():
    user="raj"
    stuff="This Some Random shitt!!"
    food=["pizza","samosa","jeraa","vadapav","khachori"]
    return render_template('home_page.html'
                           ,users_name=user, stuff=stuff, food=food )


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