from flask.helpers import url_for
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager


def scrape_all():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    movie_title, budget, budget_bins = budget_movie(browser)

    data = {
        "movie_title": movie_title,
        "budget": budget,
        "budget_bins": budget_bins(),
     }

    browser.quit()
    return data
