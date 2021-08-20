from flask.helpers import url_for
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask, render_template

# Create an instance of Flask
app = Flask(__name__)

# Route to index.html template
@app.route("/")
def index():
  # Return index template
  return render_template("low.html")

file_to_load = "data_cleaning\export\movie_db.csv"
lowest_budget = pd.read_csv(file_to_load)

lowest_total_budget = lowest_budget.loc[:, ["title", "budget", "budget_bins", "popularity"]]
#print(lowest_total_budget)

popular_low_budget = lowest_total_budget.sort_values("popularity", ascending=True).nsmallest(10, "popularity")
popular_sorted = popular_low_budget.sort_values("budget", ascending=True)
print(popular_sorted)
print(popular_low_budget)

#lowest_budget_sorted = lowest_total_budget.sort_values("budget", ascending=True).nsmallest(10, "budget")
#print(lowest_budget_sorted)
#lowest_budget_sorted.to_html("low.html")
#html_file = lowest_budget_sorted.to_html()

#least_popular = lowest_total_budget.sort_values()
#popular_sorted = least_popular.sort_values("budget", ascending=True)
#print(popular_sorted)
#print(least_popular)