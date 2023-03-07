from wtforms import SelectField, StringField, IntegerField, SelectMultipleField, FieldList, RadioField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, NumberRange, Optional


class RecipeByIngredientForm(FlaskForm):
    ingredients = StringField("Ingredients", validators = [InputRequired()])
    number = IntegerField("Number of Recipes (Max 10)", validators = [InputRequired(), NumberRange(min=1, max=10)])
    
class RandomRecipe(FlaskForm):
    diet_tag = SelectField("Have a specific diet? ", choices = [(None, 'Any'),
        ('vegetarian', 'Vegetarian'),
                                                            ('Gluten Free', 'Gluten Free'),
                                                            ('Ketogenic', 'Ketogenic'),
                                                            ('Vegan', 'Vegan'),
                                                            ('Pescetarian', 'Pescetarian'),
                                                            ('Paleo', 'Paleo')]
,
                                                            validators = [Optional()])
    meal_type_tag = SelectField("Craving Dessert?", choices =[ (None, 'Any'),                                                       ('main course', 'Main Course'),
                                                            ('side dish' , 'Side Dish'),
                                                            ('dessert' , 'Dessert'),
                                                            ('appetizer' , 'Appetizer'),
                                                            ('salad' , 'Salad'),
                                                            ('bread' ,'Bread'),
                                                            ('breakfast', 'Breakfast'),
                                                            ('soup' , 'Soup'),
                                                            ('beverage' , 'Beverage'),
                                                            ('sauce' , 'Sauce'),
                                                            ('marinade' , 'Marinade'),
                                                            ('fingerfood' , 'Fingerfood'),
                                                            ('snack' , 'Snack'),
                                                            ('drink' , 'Drink')],
                                                            validators = [Optional()])
    
    
