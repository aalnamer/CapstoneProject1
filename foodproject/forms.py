from wtforms import SelectField, StringField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired


class RecipeByIngredientForm(FlaskForm):
    ingredients = StringField("Ingredients", validators = [InputRequired()])
    number = IntegerField("Number of Recipes", validators = [InputRequired()])