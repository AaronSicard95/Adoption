from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import AnyOf

class AddPetForm(FlaskForm):

    name = StringField("Pet Name")
    species = StringField("Species", validators=[AnyOf(values=['cat', 'dog', 'porcupine'],message="not valid species")])
    photo_url = StringField("Photo URL")
    age = IntegerField("Age")
    notes = StringField("Notes")
    available = BooleanField("Available?")