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

# class DataStore():
#     city = ""
#     state = ""

#     def __repr__(self):
#         return "city: " + self.city 


# data = DataStore()

@app.route('/api', methods=['GET', 'POST'])
def api():
    user = {'username': 'Jeff'}
    form = AddressForm()
    if form.validate_on_submit():
        city = request.form.get('City')
        state = request.form.get('State')
        print(data)
        api_requested = rental_rates_via_city(data.city, data.state, 'traditional')
        return render_template('form_submit.html', api_requested=api_requested, user=user)
    return render_template('api.html', title='API', form=form, user=user)

