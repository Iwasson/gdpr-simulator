from flask import Flask, render_template
from .functions.schema_generator import generate_schema
from .functions.database_seeder import seed_db
from .functions.analytics import display_histogram

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("home_page.html"), 200

@app.route("/generate")
def generate_scheme():
    print(generate_schema(10))
    return

@app.route("/populate")
def populate_db():
    seed_db(100, 10, 5)
    return "test"

@app.route("/delete")
def delete_data():
    return