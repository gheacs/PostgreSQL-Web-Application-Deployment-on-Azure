from flask import Flask, render_template
from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Construct the database URI
db_uri = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

# Print the constructed PostgreSQL URI for debugging
print("Constructed PostgreSQL URI:", app.config['SQLALCHEMY_DATABASE_URI'])

db = SQLAlchemy(app)

# Define your model
class Event(db.Model):
    __tablename__ = 'event'  # Explicitly set the table name to 'event'
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(255))
    event_date = db.Column(db.Date)
    event_location = db.Column(db.String(255))
    event_type = db.Column(db.String(255))  # Adjusted column name to match the database
    event_region = db.Column(db.String(255))
    location_longitude = db.Column(db.Float)
    location_latitude = db.Column(db.Float)
    temperature = db.Column(db.Float)
    min_temperature = db.Column(db.Float)
    max_temperature = db.Column(db.Float)
    humidity = db.Column(db.Integer)
    description = db.Column(db.String(255))
    weather_description_new = db.Column(db.String(255))  # Adjusted column name to match the database

# Define your routes and views
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/category')
def category_chart():
    # Query the database to get the count of each event category
    category_counts = db.session.query(Event.event_type, func.count(Event.event_type)).group_by(Event.event_type).all()
    # Pass the data to the template for rendering
    return render_template('category_chart.html', category_counts=category_counts)

@app.route('/month')
def month_chart():
    # Query the database to get the count of events for each month
    month_counts = db.session.query(func.date_trunc('month', func.cast(Event.event_date, db.Date)), func.count('*')).group_by(func.date_trunc('month', func.cast(Event.event_date, db.Date))).all()
    # Pass the data to the template for rendering
    return render_template('month_chart.html', month_counts=month_counts)

@app.route('/day')
def day_chart():
    # Query the database to get the count of events for each day of the week
    day_counts = db.session.query(func.date_trunc('day', func.cast(Event.event_date, db.Date)), func.count('*')).group_by(func.date_trunc('day', func.cast(Event.event_date, db.Date))).all()
    # Pass the data to the template for rendering
    return render_template('day_chart.html', day_counts=day_counts)

# Define additional routes and views for filtering data as needed

if __name__ == '__main__':
    app.run(debug=True)
