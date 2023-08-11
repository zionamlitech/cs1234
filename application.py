from flask import Flask, render_template

app = Flask(__name__)
students=[
    {
        'id':1, 'name':'kwame', 'age':'5'
    },
    {
        'id':2, 'name':'kwasi', 'age':'17'
    },
    {
        'id':3, 'name':'sesse', 'age':'25'
    }

]
@app.route("/")
def hello_isaac():
    return render_template('school.html', students=students)
@app.route("/")
def school():
    return render_template('body.html') 
    print('Students')
@app.route ("/home.html")
def home():
    return render_template('home.html') 
@app.route ("/")
def body():
    return render_template('body.html') 
 
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
