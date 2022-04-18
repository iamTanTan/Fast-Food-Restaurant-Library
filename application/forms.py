from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, FloatField, TimeField, SelectField, IntegerField)
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

class HoursForm(FlaskForm):
    previous_day = StringField('Previous Day')
    day_of_week = SelectField('Weekday', choices=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    open_time = TimeField('Start Time', validators=[InputRequired()])
    close_time = TimeField('Close Time', validators=[InputRequired()])