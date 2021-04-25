#Importing dependencies
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

# Set up flask 
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
# Tells app that we'll be connecting to our mongo using this port and uri
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# define the route for the HTML page
@app.route("/")
def index():
    # uses PyMongo to find the "mars" collection in our database
   mars = mongo.db.mars.find_one()
    # tells Flask to return an HTML template using an index.html file
   return render_template("index.html", mars=mars)

# set up our scraping route (will be the "button" of the web application)
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   #created a new variable to hold the newly scraped data
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)

# tells flask to run 
if __name__ == "__main__":
   app.run()