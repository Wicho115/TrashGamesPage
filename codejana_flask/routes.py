#from bcrypt import methods
from codejana_flask import app, db
from sre_constants import SUCCESS
from flask import Flask, render_template,redirect,url_for,flash
from codejana_flask.forms import RegistrationForm, LoginForm
from codejana_flask.models import User 
 

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('homepage.html', title='Home')



@app.route('/about')
def about():
    return render_template('About.html', title='About')


@app.route('/games')
def games():
    return render_template('games.html', title='Games')

@app.route('/about/<user>')
def user(user):
    print(user)
    return render_template('user.html', title='User')

@app.route('/register',methods=['POST','GET'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Cuenta creada satisfactoriamente{form.username.data}', category = 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register',form=form)


@app.route('/login',methods=['POST','GET'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data== 'osja1601@gmail.com' and form.password.data == '12345':
            flash (f'Login satisfactorio{form.email.data}',category ='succes')
            return redirect(url_for('user'))
        else:
            flash (f'Login insatisfactorio{form.email.data}',category ='danger')
            return redirect(url_for('homepage'))
    return render_template('login.html', title='LogIn',form=form)
