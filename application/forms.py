from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, FloatField, BooleanField,
                     RadioField, SelectField)
from wtforms.validators import InputRequired, Length

class RestaurantForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    rtype = StringField('Type', validators=[InputRequired()])
    price = SelectField('Price Range', choices=[('low', 'low'), ('medium', 'medium'), ('high', 'high')], validators=[InputRequired()])
    
class ReviewForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    rating = SelectField('Rating', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], coerce=int)

class MenuForm(FlaskForm):
    menu_type = StringField('Menu Type', validators=[InputRequired()])

class FoodItemForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    price = FloatField('Price',validators=[InputRequired()], description="Enter decimal value without $ sign")