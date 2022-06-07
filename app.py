#pip install Flask-PyMongo;


from contextlib import redirect_stdout
from re import template
from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of our Flask app.
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)

# Set route
@app.route('/')
def home():
    mars = mongo.db.collection.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars=mongo.db.mars
    hemisphere_list = scrape_mars.scrape_info()
    mars.update_one({}, {"$set": hemisphere_list}, upsert=True)
    #scraped_data_2 = scraped_data.scrape()
    #scraped_data.update_one({}, {"$set": scraped_data_2}, upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
