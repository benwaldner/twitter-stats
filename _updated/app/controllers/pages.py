from flask import render_template, Blueprint, request
from app.forms import *
blueprint = Blueprint('pages', __name__)


################
#### routes ####
################


@blueprint.route('/')
def home():
    global data, form
    form = RegisterForm(request.form)
    data = {"ticker": "AAPL"}
    return render_template('pages/home.html', data = data, form = form)


@blueprint.route('/about')
def about():
    global data
    return render_template('pages/about.html', data = data, form = form)

@blueprint.route('/charts')
def charts():
    global data
    return render_template('pages/charts.html', data = data, form = form)

@blueprint.route('/login')
def login():
    global data
    form = LoginForm(request.form)
    return render_template('forms/login.html', form=form)


@blueprint.route('/register')
def register():
    global data
    form = RegisterForm(request.form)
    return render_template('forms/register.html', form=form)


@blueprint.route('/changeticker')
def forgot():
    global data
    form = ForgotForm(request.form)
    return render_template('forms/changeticker.html', form=form)

@blueprint.route('/searchkeyword')
def searchkeywork():
    global data
    form = KwordForm(request.form)
    return render_template('forms/searchkeyword.html', form=form)

@blueprint.route('/searchtime')
def searchtime():
    global data
    form = TimeForm(request.form)
    return render_template('forms/searchtime.html', form=form)

@blueprint.route('/search')
def search():
    global data
    form = SearchForm(request.form)
    return render_template('forms/search.html', form=form)

@blueprint.route('/results', methods = ['POST'])
def results():
    global data
    res = request.form
    print(dict(res))
    return render_template('pages/charts.html')
