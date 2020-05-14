from flask import Flask, render_template, url_for
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
# @app.route('/home')
def home_page():
    return render_template('landing.html')

@app.route('/login')
def login():
    form = loginForm()
    return render_template('login.html', title='Login', form = form)

@app.route('/add_bug')
def add_bug():
    return 'Hi bug'



@app.route('/account')
def account():
    return 'account'



if __name__ == '__main__':
    app.run(debug = True)