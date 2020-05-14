from flask import Flask, render_template, url_for, redirect, flash
from forms import loginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

bug_list = [
    {
        'name' : 'Front Page Issue',
        'description' : 'html element is out of place',
        'priority' : 'Urgent',
        'assigned_users' : ['Jimmy Lam', 'John Doe'],
    },
    {
        'name' : 'css alignment',
        'description' : 'css needs to be updated',
        'priority' : 'Not urgent',
        'assigned_users' : ['John Doe'],
    }
]

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        if form.email.data == 'JimmyLam978@gmail.com' and form.password.data == 'password':
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful, please check email and password','danger')
    return render_template('login.html', title='Login', form = form)

@app.route('/home')
def home():
    return render_template("home.html", bug_list=bug_list)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/add_bug')
def add_bug():
    return 'Hi bug'



@app.route('/account')
def account():
    return 'account'



if __name__ == '__main__':
    app.run(debug = True)