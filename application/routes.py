from flask import render_template, flash, redirect, url_for, request
from application import app
from application.forms import LoginForm, AddressForm
from application.api import rental_rates_via_city 

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jeff'}
    return render_template('index.html', title='Home', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me {}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

class DataStore():
    city = None
    state = None

data = DataStore()

@app.route('/api', methods=['GET', 'POST'])
def api():
    user = {'username': 'Jeff'}
    form = AddressForm()
    if form.validate_on_submit():
        data.city = request.form.get('City')
        data.state = request.form.get('State')
        return redirect(url_for('api_request', city=data.city, state=data.state)
    return render_template('api.html', title='API', form=form, user=user)

@app.route('/api_request', methods=['GET', 'POST'])
def api_request(city, state):
    api_requested = rental_rates_via_city(city, state)
    user = {'username': 'Jeff'}
    if request.method == 'GET':
        pass
    return render_template('form_submit.html', api_request=api_requested, user=user )


