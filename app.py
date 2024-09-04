from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import requests

app = Flask(__name__)

client = MongoClient("mongodb+srv://adelformat541:cTnyX0Pe5JqFe4bO@cluster0.xuct9.mongodb.net/flasktuto")

# conexion avec la base de donner
db = client['flasktuto']
todos = db['todos']


# create first route to submit the form

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        todos.insert_one({'email': email, 'password': password})
        return redirect(url_for('get_msg'))  # Rediriger vers une page de succès

    all_todos = todos.find()
    return render_template('index.html', todos=all_todos)

# create a success page to redirect to when the user is logged in (fake)
@app.route('/success')
def get_msg():
    return render_template('success.html')

if __name__ == '__main__':
    app.run()