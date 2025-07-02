from flask import Flask, render_template, request, redirect, session
from models import register_user, login_user, search_stations

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        register_user(request.form['username'], request.form['email'], request.form['password'])
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = login_user(request.form['email'], request.form['password'])
        if user:
            session['user'] = user[1]
            return redirect('/dashboard')
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    stations = []
    if request.method == 'POST':
        query = request.form['query']
        stations = search_stations(query)
    return render_template('dashboard.html', stations=stations)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
