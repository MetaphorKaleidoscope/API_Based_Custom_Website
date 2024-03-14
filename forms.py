from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired
import pandas as pd


data = pd.read_csv('lord_of_the_rings.csv')
characters_list = data.name.astype(str).to_string(index=False)
characters = []
char_list = list(characters_list.split("\n"))
for character in char_list:
    character.strip()
    characters.append(character.strip())


#  WTForm
class ToolsForm(FlaskForm):
    character = SelectField("Character", validators=[DataRequired()], choices=characters)
    submit = SubmitField(label="FIND THEM!")

