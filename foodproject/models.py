from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)



class Ingredient(db.Model):
    __tablename__ = "ingredients"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.Text, nullable=False)

   
    def serialize(self):
        return{
            "id" : self.id,
            "amount": self.amount,
            "unit": self.unit,
        }
        
class RecipeByIngredients(db.Model):
    __tablename__ = 'recipes_by_ingredients'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ingredients = db.Column(db.Text, nullable = False)
    number = db.Column(db.Integer, nullable = False)
       
    def serialize(self):
        return{
            "id" : self.id,
            "ingredients": self.ingredients,
            "number": self.number,
        }
        
        
class Recipe(db.Model):
    __tablename__ = 'recipes'
    table_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id = db.Column(db.Integer, nullable = False)
    
    def serialize(self):
        return{
            "id" : self.id
        }