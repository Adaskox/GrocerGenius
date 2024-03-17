import csv
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///groceries.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate
csv_path = r'C:\Users\Adaskox\GrocerGenius\FilteredIngr.csv'  # Update this path to your CSV file's location

class Grocery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meal = db.Column(db.String(100), nullable=False)  # This should be your primary key or unique if it will always be unique
    ingredient = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.String(100), nullable=False)
    ingredient2 = db.Column(db.String(100), nullable=True)
    amount2 = db.Column(db.String(100), nullable=True)

def import_groceries_from_csv(csv_path):
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            grocery_item = Grocery(
                meal=row['meal'],
                ingredient=row['ingredient'],
                amount=row['amount'],
                ingredient2=row['ingredient2'],
                amount2=row['amount2']
            )
            db.session.add(grocery_item)
        db.session.commit()


@app.route('/')
def show_groceries():
    groceries = Grocery.query.all()
    return render_template('groceries.html', groceries=groceries)

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
    with app.app_context():
        db.create_all()
        import_groceries_from_csv(csv_path)
    app.run(debug=True)
