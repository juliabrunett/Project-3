#import psycopg2
#from sqlalchemy import create_engine
import pandas as pd
from flask import Flask, render_template
#from config import db_user, db_password, db_host, db_port, db_name

# Database setup
#engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# Create an instance of Flask
app = Flask(__name__)

# Route to index.html template
@app.route("/")
def index():
  # Return index template
  return render_template("index.html")

# Route to movie_dataset.csv
@app.route("/api/movie_dataset")
def movie_dataset():
  # Read csv in to pandas dataframe
  results_df = pd.read_csv("resources/movie_dataset.csv")
  # Convert results to json (orient = 'records' get an dictonary/object for each row of dataframe)
  results_json = results_df.to_json(orient='records') 
  return results_json

# Route to female focused
@app.route("/femalefocused")
def femalefocused():
  # Direct to femalefocused.html
  return render_template("femalefocused.html")

# Route to international
@app.route("/international")
def international():
  # Direct to international.html
  return render_template("international.html")

# Route to low budget
@app.route("/lowbudget")
def lowbudget():
  # Direct to lowbudget.html
  return render_template("lowbudget.html")

if __name__ == "__main__":
  app.run(debug=True)