from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length


class RegisterForm(Form):
    name = TextField(
        'Username', validators=[DataRequired(), Length(min=6, max=25)]
    )
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=6, max=40)]
    )
    confirm = PasswordField(
        'Repeat Password',
        [DataRequired(),
        EqualTo('password', message='Passwords must match')]
    )



class LoginForm(Form):
    name = TextField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])


class ForgotForm(Form):
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )

class KwordForm(Form):
    keyword = TextField(
        'Keyword', validators=[DataRequired(), Length(min=0, max=40)]
    )

class TimeForm(Form):
    start = TextField('Start', [DataRequired()])
    end = TextField('End', [DataRequired()])

class SearchForm(Form):
    ticker = TextField('Ticker', [DataRequired()])
    keyword = TextField('Keyword', [DataRequired()])
    start = TextField('Start', [DataRequired()])
    end = TextField('End', [DataRequired()])
