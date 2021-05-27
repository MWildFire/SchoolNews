from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def entry_point():
    return render_template('community.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register_person')
def register_person():
    return render_template('register_person.html')

if __name__ == '__main__':
    app.run(debug=True)