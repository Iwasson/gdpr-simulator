import time

from flask import Flask, render_template, request
from .functions.database_seeder import seed_db
from .functions.sqlite_wrapper import get_first_n_rows

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("home_page.html"), 200


@app.route("/generate", methods=["POST"])
def generate_schema():
    start_time = time.time()
    num_columns = int(request.form["num_columns"])
    num_rows = int(request.form["num_rows"])
    linking_strength = int(request.form["linking_strength"])
    link_deviation = int(50 - linking_strength / 100 * 50)
    schema = seed_db(num_rows, num_columns, link_deviation)
    top_rows = get_first_n_rows(10)
    end_time = time.time()

    time_diff_count = end_time - start_time
    time_diff = f"{time_diff_count:.2f} Seconds"

    # print(get_first_n_rows(10))
    return render_template(
        "display.html",
        num_columns=num_columns,
        num_rows=num_rows,
        link_deviation=link_deviation,
        schema=schema,
        top_rows=top_rows,
        time_diff=time_diff,
    )


@app.route("/populate")
def populate_db():
    seed_db(100, 10, 5)
    return "test"


@app.route("/delete")
def delete_data():
    return
