from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional

class AddCupcake(FlaskForm):
    flavor = StringField("Flavor")
    size = StringField("Size")
    rating = FloatField('rating')
    image = StringField("Image")
