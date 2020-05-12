from flask import Flask, render_template

app = Flask(__name__)

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
@app.route('/home')
def home_page():
    return render_template('home.html', bug_list = bug_list)


@app.route('/add_bug')
def add_bug():
    return 'Hi bug'

@app.route('/login')
def login():
    return 'login'

@app.route('/account')
def account():
    return 'account'



if __name__ == '__main__':
    app.run(debug = True)