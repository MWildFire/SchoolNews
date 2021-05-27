from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def entry_point():
    return render_template('community.html')


@app.route('/register_person')
def register_person():
    return render_template('register_person.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        pass


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        pass


@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'GET':
        return render_template('forgot_password.html')
    else:
        pass



if __name__ == '__main__':
    app.run(debug=True)