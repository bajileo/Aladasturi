from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Length, EqualTo

class RegisterF(FlaskForm):
    nickname = StringField(label="Nickname:", validators=[Length(min = 4, max = 12)] )
    password = PasswordField(label="Password:", validators=[Length(min = 5)] )
    rpassword = PasswordField(label="Repeat Password:", validators=[EqualTo("password")] )
    register = SubmitField(label="Register")

class LoginF(FlaskForm):
    nickname = StringField(label="Nickname:")
    password = PasswordField(label="Password:")
    login = SubmitField(label="Login")

class AddReview(FlaskForm):
    reviewc = StringField(label="Your review:", validators=[Length(max = 52)] )
    submit = SubmitField(label="submit")

class Discount(FlaskForm):
    discount_code = StringField(label="Discount-Coupon:", validators=[Length(min=8, max=8)] )
    use = SubmitField(label="Use")

def __str__(self):
    return f"{self.nickname}"
